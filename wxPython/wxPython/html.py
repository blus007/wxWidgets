## This file reverse renames symbols in the wx package to give
## them their wx prefix again, for backwards compatibility.
##
## Generated by ./distrib/build_renamers.py

# This silly stuff here is so the wxPython.wx module doesn't conflict
# with the wx package.  We need to import modules from the wx package
# here, then we'll put the wxPython.wx entry back in sys.modules.
import sys
_wx = None
if sys.modules.has_key('wxPython.wx'):
    _wx = sys.modules['wxPython.wx']
    del sys.modules['wxPython.wx']

import wx.html

sys.modules['wxPython.wx'] = _wx
del sys, _wx


# Now assign all the reverse-renamed names:
wxHtmlWindowNameStr = wx.html.HtmlWindowNameStr
wxHtmlPrintoutTitleStr = wx.html.HtmlPrintoutTitleStr
wxHtmlPrintingTitleStr = wx.html.HtmlPrintingTitleStr
wxHTML_ALIGN_LEFT = wx.html.HTML_ALIGN_LEFT
wxHTML_ALIGN_CENTER = wx.html.HTML_ALIGN_CENTER
wxHTML_ALIGN_RIGHT = wx.html.HTML_ALIGN_RIGHT
wxHTML_ALIGN_BOTTOM = wx.html.HTML_ALIGN_BOTTOM
wxHTML_ALIGN_TOP = wx.html.HTML_ALIGN_TOP
wxHTML_CLR_FOREGROUND = wx.html.HTML_CLR_FOREGROUND
wxHTML_CLR_BACKGROUND = wx.html.HTML_CLR_BACKGROUND
wxHTML_UNITS_PIXELS = wx.html.HTML_UNITS_PIXELS
wxHTML_UNITS_PERCENT = wx.html.HTML_UNITS_PERCENT
wxHTML_INDENT_LEFT = wx.html.HTML_INDENT_LEFT
wxHTML_INDENT_RIGHT = wx.html.HTML_INDENT_RIGHT
wxHTML_INDENT_TOP = wx.html.HTML_INDENT_TOP
wxHTML_INDENT_BOTTOM = wx.html.HTML_INDENT_BOTTOM
wxHTML_INDENT_HORIZONTAL = wx.html.HTML_INDENT_HORIZONTAL
wxHTML_INDENT_VERTICAL = wx.html.HTML_INDENT_VERTICAL
wxHTML_INDENT_ALL = wx.html.HTML_INDENT_ALL
wxHTML_COND_ISANCHOR = wx.html.HTML_COND_ISANCHOR
wxHTML_COND_ISIMAGEMAP = wx.html.HTML_COND_ISIMAGEMAP
wxHTML_COND_USER = wx.html.HTML_COND_USER
wxHTML_FONT_SIZE_1 = wx.html.HTML_FONT_SIZE_1
wxHTML_FONT_SIZE_2 = wx.html.HTML_FONT_SIZE_2
wxHTML_FONT_SIZE_3 = wx.html.HTML_FONT_SIZE_3
wxHTML_FONT_SIZE_4 = wx.html.HTML_FONT_SIZE_4
wxHTML_FONT_SIZE_5 = wx.html.HTML_FONT_SIZE_5
wxHTML_FONT_SIZE_6 = wx.html.HTML_FONT_SIZE_6
wxHTML_FONT_SIZE_7 = wx.html.HTML_FONT_SIZE_7
wxHW_SCROLLBAR_NEVER = wx.html.HW_SCROLLBAR_NEVER
wxHW_SCROLLBAR_AUTO = wx.html.HW_SCROLLBAR_AUTO
wxHW_NO_SELECTION = wx.html.HW_NO_SELECTION
wxHW_DEFAULT_STYLE = wx.html.HW_DEFAULT_STYLE
wxHTML_OPEN = wx.html.HTML_OPEN
wxHTML_BLOCK = wx.html.HTML_BLOCK
wxHTML_REDIRECT = wx.html.HTML_REDIRECT
wxHTML_URL_PAGE = wx.html.HTML_URL_PAGE
wxHTML_URL_IMAGE = wx.html.HTML_URL_IMAGE
wxHTML_URL_OTHER = wx.html.HTML_URL_OTHER
wxHtmlLinkInfo = wx.html.HtmlLinkInfo
wxHtmlLinkInfoPtr = wx.html.HtmlLinkInfoPtr
wxHtmlTag = wx.html.HtmlTag
wxHtmlTagPtr = wx.html.HtmlTagPtr
wxHtmlParser = wx.html.HtmlParser
wxHtmlParserPtr = wx.html.HtmlParserPtr
wxHtmlWinParser = wx.html.HtmlWinParser
wxHtmlWinParserPtr = wx.html.HtmlWinParserPtr
wxHtmlTagHandler = wx.html.HtmlTagHandler
wxHtmlTagHandlerPtr = wx.html.HtmlTagHandlerPtr
wxHtmlWinTagHandler = wx.html.HtmlWinTagHandler
wxHtmlWinTagHandlerPtr = wx.html.HtmlWinTagHandlerPtr
wxHtmlWinParser_AddTagHandler = wx.html.HtmlWinParser_AddTagHandler
wxHtmlSelection = wx.html.HtmlSelection
wxHtmlSelectionPtr = wx.html.HtmlSelectionPtr
wxHTML_SEL_OUT = wx.html.HTML_SEL_OUT
wxHTML_SEL_IN = wx.html.HTML_SEL_IN
wxHTML_SEL_CHANGING = wx.html.HTML_SEL_CHANGING
wxHtmlRenderingState = wx.html.HtmlRenderingState
wxHtmlRenderingStatePtr = wx.html.HtmlRenderingStatePtr
wxHtmlRenderingStyle = wx.html.HtmlRenderingStyle
wxHtmlRenderingStylePtr = wx.html.HtmlRenderingStylePtr
wxDefaultHtmlRenderingStyle = wx.html.DefaultHtmlRenderingStyle
wxDefaultHtmlRenderingStylePtr = wx.html.DefaultHtmlRenderingStylePtr
wxHtmlRenderingInfo = wx.html.HtmlRenderingInfo
wxHtmlRenderingInfoPtr = wx.html.HtmlRenderingInfoPtr
wxHTML_FIND_EXACT = wx.html.HTML_FIND_EXACT
wxHTML_FIND_NEAREST_BEFORE = wx.html.HTML_FIND_NEAREST_BEFORE
wxHTML_FIND_NEAREST_AFTER = wx.html.HTML_FIND_NEAREST_AFTER
wxHtmlCell = wx.html.HtmlCell
wxHtmlCellPtr = wx.html.HtmlCellPtr
wxHtmlWordCell = wx.html.HtmlWordCell
wxHtmlWordCellPtr = wx.html.HtmlWordCellPtr
wxHtmlContainerCell = wx.html.HtmlContainerCell
wxHtmlContainerCellPtr = wx.html.HtmlContainerCellPtr
wxHtmlColourCell = wx.html.HtmlColourCell
wxHtmlColourCellPtr = wx.html.HtmlColourCellPtr
wxHtmlFontCell = wx.html.HtmlFontCell
wxHtmlFontCellPtr = wx.html.HtmlFontCellPtr
wxHtmlWidgetCell = wx.html.HtmlWidgetCell
wxHtmlWidgetCellPtr = wx.html.HtmlWidgetCellPtr
wxHtmlFilter = wx.html.HtmlFilter
wxHtmlFilterPtr = wx.html.HtmlFilterPtr
wxHtmlWindow = wx.html.HtmlWindow
wxHtmlWindowPtr = wx.html.HtmlWindowPtr
wxPreHtmlWindow = wx.html.PreHtmlWindow
wxHtmlWindow_AddFilter = wx.html.HtmlWindow_AddFilter
wxHtmlWindow_GetClassDefaultAttributes = wx.html.HtmlWindow_GetClassDefaultAttributes
wxHtmlDCRenderer = wx.html.HtmlDCRenderer
wxHtmlDCRendererPtr = wx.html.HtmlDCRendererPtr
wxPAGE_ODD = wx.html.PAGE_ODD
wxPAGE_EVEN = wx.html.PAGE_EVEN
wxPAGE_ALL = wx.html.PAGE_ALL
wxHtmlPrintout = wx.html.HtmlPrintout
wxHtmlPrintoutPtr = wx.html.HtmlPrintoutPtr
wxHtmlPrintout_AddFilter = wx.html.HtmlPrintout_AddFilter
wxHtmlPrintout_CleanUpStatics = wx.html.HtmlPrintout_CleanUpStatics
wxHtmlEasyPrinting = wx.html.HtmlEasyPrinting
wxHtmlEasyPrintingPtr = wx.html.HtmlEasyPrintingPtr
wxHtmlBookRecord = wx.html.HtmlBookRecord
wxHtmlBookRecordPtr = wx.html.HtmlBookRecordPtr
wxHtmlContentsItem = wx.html.HtmlContentsItem
wxHtmlContentsItemPtr = wx.html.HtmlContentsItemPtr
wxHtmlSearchStatus = wx.html.HtmlSearchStatus
wxHtmlSearchStatusPtr = wx.html.HtmlSearchStatusPtr
wxHtmlHelpData = wx.html.HtmlHelpData
wxHtmlHelpDataPtr = wx.html.HtmlHelpDataPtr
wxHtmlHelpFrame = wx.html.HtmlHelpFrame
wxHtmlHelpFramePtr = wx.html.HtmlHelpFramePtr
wxHF_TOOLBAR = wx.html.HF_TOOLBAR
wxHF_FLATTOOLBAR = wx.html.HF_FLATTOOLBAR
wxHF_CONTENTS = wx.html.HF_CONTENTS
wxHF_INDEX = wx.html.HF_INDEX
wxHF_SEARCH = wx.html.HF_SEARCH
wxHF_BOOKMARKS = wx.html.HF_BOOKMARKS
wxHF_OPENFILES = wx.html.HF_OPENFILES
wxHF_PRINT = wx.html.HF_PRINT
wxHF_DEFAULTSTYLE = wx.html.HF_DEFAULTSTYLE
wxHtmlHelpController = wx.html.HtmlHelpController
wxHtmlHelpControllerPtr = wx.html.HtmlHelpControllerPtr


