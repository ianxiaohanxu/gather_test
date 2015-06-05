import unittest, sys, warnings


class SkipTest(Exception):
    """
    Raise this exception in a test to skip it.

    Usually you can use TestCase.skipTest() or one of the skipping decorators
    instead of raising this directly.
    """
    pass

class _ExpectedFailure(Exception):
    """
    Raise this when a test is expected to fail.

    This is an implementation detail.
    """

    def __init__(self, exc_info):
        super(_ExpectedFailure, self).__init__()
        self.exc_info = exc_info

class _UnexpectedSuccess(Exception):
    """
    The test was supposed to fail, but it didn't!
    """
    pass

class Case(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        self._testMethodName = methodName
        self._resultForDoCleanups = None
        try:
            testMethod = getattr(self, methodName)
        except AttributeError:
            raise ValueError("no such test method in %s: %s" %
                  (self.__class__, methodName))
        self._testMethodDoc = testMethod.__doc__
        self._cleanups = []

        # Map types to custom assertEqual functions that will compare
        # instances of said type in more detail to generate a more useful
        # error message.
        self._type_equality_funcs = {}
        self.addTypeEqualityFunc(dict, 'assertDictEqual')
        self.addTypeEqualityFunc(list, 'assertListEqual')
        self.addTypeEqualityFunc(tuple, 'assertTupleEqual')
        self.addTypeEqualityFunc(set, 'assertSetEqual')
        self.addTypeEqualityFunc(frozenset, 'assertSetEqual')
        try:
            self.addTypeEqualityFunc(unicode, 'assertMultiLineEqual')
        except NameError:
            # No unicode support in this build
            pass
        self._repeat_count = 3
        
    def run(self, result=None):
        orig_result = result
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

        self._resultForDoCleanups = result
        result.startTest(self)

        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or
            getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, skip_why)
            finally:
                result.stopTest(self)
            return
        try:
            while(self._repeat_count > 0):
                success = False
                try:
                    self.setUp()
                except SkipTest as e:
                    self._addSkip(result, str(e))
                    self._repeat_count = 0
                except KeyboardInterrupt:
                    raise
                    self._repeat_count = 0
                except:
                    result.addError(self, sys.exc_info())
                    self._repeat_count = 0
                else:
                    try:
                        testMethod()
                    except KeyboardInterrupt:
                        raise
                        self._repeat_count = 0
                    except self.failureException:
                        if self._repeat_count == 1:
                            result.addFailure(self, sys.exc_info())
                        self._repeat_count -= 1
                    except _ExpectedFailure as e:
                        addExpectedFailure = getattr(result, 'addExpectedFailure', None)
                        if addExpectedFailure is not None:
                            addExpectedFailure(self, e.exc_info)
                        else:
                            warnings.warn("TestResult has no addExpectedFailure method, reporting as passes",
                                          RuntimeWarning)
                            result.addSuccess(self)
                        self._repeat_count = 0
                    except _UnexpectedSuccess:
                        addUnexpectedSuccess = getattr(result, 'addUnexpectedSuccess', None)
                        if addUnexpectedSuccess is not None:
                            addUnexpectedSuccess(self)
                        else:
                            warnings.warn("TestResult has no addUnexpectedSuccess method, reporting as failures",
                                          RuntimeWarning)
                            result.addFailure(self, sys.exc_info())
                        self._repeat_count = 0
                    except SkipTest as e:
                        self._addSkip(result, str(e))
                        self._repeat_count = 0
                    except:
                        if self._repeat_count == 1:
                            result.addError(self, sys.exc_info())
                        self._repeat_count -= 1
                    else:
                        success = True
                        self._repeat_count = 0

                    try:
                        self.tearDown()
                    except KeyboardInterrupt:
                        raise
                        self._repeat_count = 0
                    except:
                        result.addError(self, sys.exc_info())
                        self._repeat_count = 0
                        success = False

                cleanUpSuccess = self.doCleanups()
                success = success and cleanUpSuccess
                if success:
                    result.addSuccess(self)
                
        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()