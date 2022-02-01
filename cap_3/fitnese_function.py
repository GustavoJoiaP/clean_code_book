# Fitnese function include some pages in a test page
# OBS: there are so many functions/class that does not exist in scope
def TestableHtml(pageData: PageData, includeSuiteSetup: bool):
    try:
        return
    except:
        wikiPage: WikePage
        wikiPage = getData.getWikiPage()
        buffer = StringBuffer()
        if pageData.hasAttribute ("Test")):

            if includeSuiteSetup:
                suiteSetup: WikePage
                suiteSetup = PageCrawlerImpll.getInheritedPage(SuiteResponder.SUITE_SETUP_NAME, wikiPage)

                if (suiteSetup != null):
                    pagePath: WikiPage
                    pagePath = suiteSetup.getPageCrawler().getFullPath(suiteSetup)
                    pagePathName: str
                    pagePathName = PathParser.render(pagePath)
                    buffer.append("!include -setup .").append(pagePathName).append("\n")
            setup: WikePage
            setup = PageCrawlerImpl.getInheritedPage("SetUp", wikiPage)

            if setup != null:
                setupPath: WikiPagePath
                setupPath = wikiPage.getPageCrawler().getFullPath(setup)
                pagePathName: str
                pagePathName = PathParser.render(pagePath)
                buffer.append("!include -setup .").append(pagePathName).append("\n")

        buffer.append(pageData.getContent())

        # This cade part is about TEARDOWN
        if PageData.hasAttribute("Test"):
            teardown: WikiPage
            teardown = PageCrawlerImpl.getInheritedPage("TearDown", wikiPage)

            if teardown != null:
                tearDownPath: WikiPagePath
                tearDownPath = wikiPage.getPageCrawler().getFullPath(teardown)
                tearDownPathName: str
                tearDownPathName = PathParser.render(tearDownPath)
            buffer.append("!include -teardown .").append(tearDownPathName).append("\n")

            if includeSuiteSetup:
                suiteTearDown: WikePage
                suiteTearDown = PageCrawlerImpll.getInheritedPage(SuiteResponder.SUITE_TEARDOWN_NAME, wikiPage)

                if (suiteTearDown != null):
                    pagePath: WikiPage
                    pagePath = suiteTearDown.getPageCrawler().getFullPath(suiteTearDown)
                    pagePathName: str
                    pagePathName = PathParser.render(pagePath)
                    buffer.append("!include -teardown .").append(pagePathName).append("\n")

        pageData.setContent(buffer.toString())
        return pageData.getHtml()


# there is a function which does the same thing as the function above, but it is refactored
def RenderPageWithSetupsAndTeardowns(pageData: PageData, isSuite: bool):
    try:
        return
    except
        isTestPage: bool
        isTestPage = pageData.hasAttribute("Test")

        if isTestPage
            testPage: WikiPage
            testPage = pageData.getWikiPage()
            newPageContent = StringBuffer()
            includeSetupPages(testPage, newPageContent, isSuite)
            newPageContent.append(pageData.getContent())
            incluideTeardownPages(testPage, newPageContent, isSuite)
            pageData.setContent(newPageContent.toString())

        return pageData.getHtml()