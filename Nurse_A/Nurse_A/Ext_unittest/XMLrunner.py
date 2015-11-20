import xmlrunner, time

class XMLTestResult(xmlrunner.result._XMLTestResult):

    def _prepare_callback(self, test_info, target_list, verbose_str,
                          short_str):
        """
        Appends a _TestInfo to the given target list and sets a callback
        method to be called by stopTest method.
        """
        target_list.append(test_info)

        def callback():
            """Prints the test method outcome to the stream, as well as
            the elapsed time.
            """

            test_info.test_finished()

            # Ignore the elapsed times for a more reliable unit testing
            if not self.elapsed_times:
                self.start_time = self.stop_time = 0

            if self.showAll:
                self.stream.writeln(
                    '%s (%.3fs) %s' % (verbose_str, test_info.elapsed_time, self._start_time)
                )
            elif self.dots:
                self.stream.write(short_str)
        self.callback = callback

    def startTest(self, test):
        """
        Called before execute each test method.
        """
        self.start_time = time.time()
        self._start_time = time.strftime("%Y%m%d%H%M%S")
        xmlrunner.unittest.TestResult.startTest(self, test)

        if self.showAll:
            self.stream.write('  ' + self.getDescription(test))
            self.stream.write(" ... ")

class xmlTestRunner(xmlrunner.XMLTestRunner):
    """
    A test runner class that outputs the results in JUnit like XML files.
    """
    def _make_result(self):
        """
        Creates a TestResult object which will be used to store
        information about the executed tests.
        """
        return XMLTestResult(
            self.stream, self.descriptions, self.verbosity, self.elapsed_times
        )
