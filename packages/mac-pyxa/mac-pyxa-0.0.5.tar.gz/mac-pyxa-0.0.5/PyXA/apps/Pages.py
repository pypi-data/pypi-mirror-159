""".. versionadded:: 0.0.2

Control the macOS Keynote application using JXA-like syntax.
"""
from cgitb import text
from enum import Enum
from time import sleep
from typing import Any, List, Tuple, Union
from AppKit import NSURL, NSSet, NSPoint, NSValue

from PyXA import XABase
from PyXA.XABase import OSType
from PyXA import XABaseScriptable

class XAPagesApplication(XABaseScriptable.XASBApplication, XABase.XAAcceptsPushedElements, XABase.XACanConstructElement, XABase.XACanOpenPath):
    """A class for managing and interacting with Keynote.app.

    .. seealso:: :class:`XAPagesWindow`, :class:`XAPagesDocument`

    .. versionadded:: 0.0.2
    """
    class SaveOption(Enum):
        """Options for what to do when calling a save event.
        """
        SAVE_FILE   = OSType('yes ') #: Save the file. 
        DONT_SAVE   = OSType('no  ') #: Do not save the file. 
        ASK         = OSType('ask ') #: Ask the user whether or not to save the file. 

    class ExportFormat(Enum):
        """Options for what format to export a Keynote project as.
        """
        KEYNOTE                 = OSType('Knff') # The Keynote native file format 
        HTML                    = OSType('Khtm') # HTML 
        QUICKTIME_MOVIE         = OSType('Kmov') # QuickTime movie 
        PDF                     = OSType('Kpdf') # PDF 
        SLIDE_IMAGES            = OSType('Kimg') # image 
        MICROSOFT_POWERPOINT    = OSType('Kppt') # Microsoft PowerPoint 
        KEYNOTE_09              = OSType('Kkey') # Keynote 09 
        JPEG                    = OSType('Kifj') # JPEG 
        PNG                     = OSType('Kifp') # PNG 
        TIFF                    = OSType('Kift') # TIFF 
        f360p                   = OSType('Kmf3') # 360p 
        f540p                   = OSType('Kmf5') # 540p 
        f720p                   = OSType('Kmf7') # 720p 
        f1080p                  = OSType('Kmf8') # 1080p 
        f2160p                  = OSType('Kmf4') # DCI 4K (4096x2160) 
        NativeSize              = OSType('KmfN') # Exported movie will have the same dimensions as the document, up to 4096x2160 

    class Codec(Enum):
        """Options for which video codec to use.
        """
        H264                    = OSType('Kmc1') # H.264 
        APPLE_PRO_RES_422       = OSType('Kmc2') # Apple ProRes 422 
        APPLE_PRO_RES_4444      = OSType('Kmc3') # Apple ProRes 4444 
        APPLE_PRO_RES_422LT     = OSType('Kmc4') # Apple ProRes 422LT 
        APPLE_PRO_RES_422HQ     = OSType('Kmc5') # Apple ProRes 422HQ 
        APPLE_PRO_RES_422Proxy  = OSType('Kmc6') # Apple ProRes 422Proxy 
        HEVC                    = OSType('Kmc7') # HEVC 

    class Framerate(Enum):
        """Options for which framerate to use when exporting a Keynote project as a video.
        """
        FPS_12     = OSType('Kfr1') # 12 FPS 
        FPS_2398   = OSType('Kfr2') # 23.98 FPS 
        FPS_24     = OSType('Kfr3') # 24 FPS 
        FPS_25     = OSType('Kfr4') # 25 FPS 
        FPS_2997   = OSType('Kfr5') # 29.97 FPS 
        FPS_30     = OSType('Kfr6') # 30 FPS 
        FPS_50     = OSType('Kfr7') # 50 FPS 
        FPS_5994   = OSType('Kfr8') # 59.94 FPS 
        FPS_60     = OSType('Kfr9') # 60 FPS 

    class PrintSetting(Enum):
        """Options to use when printing slides.
        """
        STANDARD_ERROR_HANDLING = OSType('lwst') # Standard PostScript error handling 
        DETAILED_ERROR_HANDLING = OSType('lwdt') # print a detailed report of PostScript errors 
        INDIVIDUAL_SLIDES       = OSType('Kpwi') # individual slides 
        SLIDE_WITH_NOTES        = OSType('Kpwn') # slides with notes 
        HANDOUTS                = OSType('Kpwh') # handouts 

    class ImageQuality(Enum):
        """Options for the quality of exported images.
        """
        GOOD      = OSType('KnP0') # good quality 
        BETTER    = OSType('KnP1') # better quality 
        BEST      = OSType('KnP2') # best quality 

    class Transition(Enum):
        """The available options for transitions to assign to slides.
        """
        NONE  = OSType('tnil') 
        MAGIC_MOVE          = OSType('tmjv')   
        SHIMMER             = OSType('tshm')  
        SPARKLE             = OSType('tspk')   
        SWING               = OSType('tswg')   
        OBJECT_CUBE         = OSType('tocb')   
        OBJECT_FLIP         = OSType('tofp')   
        OBJECT_POP          = OSType('topp')   
        OBJECT_PUSH         = OSType('toph')   
        OBJECT_REVOLVE      = OSType('torv')   
        OBJECT_ZOOM         = OSType('tozm')   
        PERSPECTIVE         = OSType('tprs')   
        CLOTHESLINE         = OSType('tclo')   
        CONFETTI            = OSType('tcft')   
        DISSOLVE            = OSType('tdis')   
        DROP                = OSType('tdrp')   
        DROPLET             = OSType('tdpl')   
        FADE_THROUGH_COLOR  = OSType('tftc')   
        GRID                = OSType('tgrd')   
        IRIS                = OSType('tirs')   
        MOVE_IN             = OSType('tmvi')   
        PUSH                = OSType('tpsh')   
        REVEAL              = OSType('trvl')   
        SWITCH              = OSType('tswi')   
        WIPE                = OSType('twpe')   
        BLINDS              = OSType('tbld')   
        COLOR_PANES         = OSType('tcpl')   
        CUBE                = OSType('tcub')   
        DOORWAY             = OSType('tdwy')   
        FALL                = OSType('tfal')   
        FLIP                = OSType('tfip')   
        FLOP                = OSType('tfop')   
        MOSAIC              = OSType('tmsc')   
        PAGE_FLIP           = OSType('tpfl')   
        PIVOT               = OSType('tpvt')   
        REFLECTION          = OSType('trfl')   
        REVOLVING_DOOR      = OSType('trev')   
        SCALE               = OSType('tscl')   
        SWAP                = OSType('tswp')   
        SWOOSH              = OSType('tsws')   
        TWIRL               = OSType('ttwl')   
        TWIST               = OSType('ttwi')   
        FADE_AND_MOVE       = OSType('tfad')   

    class Alignment(Enum):
        """Options for the horizontal and vertical alignment of content within table containers.
        """
        BOTTOM                  = OSType('avbt') #: Bottom-align content. 
        CENTER_VERTICAL         = OSType('actr') #: Center-align content. 
        TOP                     = OSType('avtp') #: Top-align content. 
        AUTO                    = OSType('aaut') #: Auto-align based on content type. 
        CENTER_HORIZONTAL       = OSType('actr') #: Center-align content. 
        JUSTIFY                 = OSType('ajst') #: Fully justify (left and right) content. 
        LEFT                    = OSType('alft') #: Left-align content. 
        RIGHT                   = OSType('arit') #: Right-align content. 

    class SortDirection(Enum):
        """Options for the direction of sorting when sorting table cells.
        """
        ASCENDING               = OSType('ascn') #: Sort in increasing value order 
        DESCENDING              = OSType('dscn') #: Sort in decreasing value order 

    class CellFormat(Enum):
        """Options for the format to use when formatting table cells.
        """
        AUTO                    = OSType('faut') #: Automatic format 
        CHECKBOX                = OSType('fcch') #: Checkbox control format (Numbers only) 
        CURRENCY                = OSType('fcur') #: Currency number format 
        DATE_AND_TIME           = OSType('fdtm') #: Date and time format 
        FRACTION                = OSType('ffra') #: Fraction number format 
        DECIMAL_NUMBER          = OSType('nmbr') #: Decimal number format 
        PERCENT                 = OSType('fper') #: Percentage number format 
        POPUP_MENU              = OSType('fcpp') #: Pop-up menu control format (Numbers only) 
        SCIENTIFIC              = OSType('fsci') #: Scientific notation format 
        SLIDER                  = OSType('fcsl') #: Slider control format (Numbers only) 
        STEPPER                 = OSType('fcst') #: Stepper control format (Numbers only) 
        TEXT                    = OSType('ctxt') #: Text format 
        DURATION                = OSType('fdur') #: Duration format 
        RATING                  = OSType('frat') #: Rating format. (Numbers only) 
        NUMERAL_SYSTEM          = OSType('fcns') #: Numeral System 

    class FillOption(Enum):
        """Options for the type of fill to use.
        """
        NO_FILL                 = OSType('fino')   
        COLOR_FILL              = OSType('fico')   
        GRADIENT_FILL           = OSType('figr')   
        ADVANCED_GRADIENT_FILL  = OSType('fiag')   
        IMAGE_FILL              = OSType('fiim')   
        ADVANCED_IMAGE_FILL     = OSType('fiai')   

    class RepetitionMethod(Enum):
        """Options for whether and how a clip will repeat.
        """
        NONE                    = OSType('mvrn')   
        LOOP                    = OSType('mvlp')   
        LOOP_BACK_AND_FORTH     = OSType('mvbf')   

    class ChartType(Enum):
        """Options for available chart types.
        """
        PIE_2D                      = OSType('pie2') #: Two-dimensional pie chart 
        VERTICAL_BAR_2D             = OSType('vbr2') #: Two-dimensional vertical bar chart 
        STACKED_VERTICAL_BAR_2D     = OSType('svb2') #: Two-dimensional stacked vertical bar chart 
        HORIZONTAL_BAR_2D           = OSType('hbr2') #: Two-dimensional horizontal bar chart 
        STACKED_HORIZONTAL_BAR_2D   = OSType('shb2') #: Two-dimensional stacked horizontal bar chart 
        PIE_3D                      = OSType('pie3') #: Three-dimensional pie chart. 
        VERTICAL_BAR_3D             = OSType('vbr3') #: Three-dimensional vertical bar chart 
        STACKED_VERTICAL_BAR_3D     = OSType('svb3') #: Three-dimensional stacked bar chart 
        HORIZONTAL_BAR_3D           = OSType('hbr3') #: Three-dimensional horizontal bar chart 
        STACKED_HORIZONTAL_BAR_3D   = OSType('shb3') #: Three-dimensional stacked horizontal bar chart 
        AREA_2D                     = OSType('are2') #: Two-dimensional area chart. 
        STACKED_AREA_2D             = OSType('sar2') #: Two-dimensional stacked area chart 
        LINE_2D                     = OSType('lin2') #: Two-dimensional line chart. 
        LINE_3D                     = OSType('lin3') #: Three-dimensional line chart 
        AREA_3D                     = OSType('are3') #: Three-dimensional area chart 
        STACKED_AREA_3D             = OSType('sar3') #: Three-dimensional stacked area chart 
        SCATTERPLOT_2D              = OSType('scp2') #: Two-dimensional scatterplot chart 

    class ChartGrouping(Enum):
        """Options for how data is grouped within a chart.
        """
        ROW      = OSType('KCgr') # group by row
        COLUMN   = OSType('KCgc') # group by column

    class KeyAction(Enum):
        """Options for key states and interactions.
        """
        COMMAND_DOWN = OSType('Kcmd')
        CONTROL_DOWN = OSType('Kctl')
        OPTION_DOWN  = OSType('Kopt')
        SHIFT_DOWN   = OSType('Ksft')

    def __init__(self, properties):
        super().__init__(properties)
        self.xa_wcls = XAPagesWindow

        self.properties = self.xa_scel.properties()
        self.name = self.properties["name"] #: The name of the Keynote application
        self.frontmost = self.properties["frontmost"] #: Whether Keynote is the active application
        self.version = self.properties["version"] #: The Keynote version number

    def show_next(self) -> 'XAPagesApplication':
        """Advance one slide or animation build.
        """
        self.xa_scel.showNext()
        return self

    def show_previous(self) -> 'XAPagesApplication':
        """Go back one slide or animation build.
        """
        self.xa_scel.showPrevious()
        return self

    def print(self, item: Union['XAPagesDocument', XABaseScriptable.XASBWindow]) -> 'XAPagesApplication':
        self.xa_scel.print_withProperties_printDialog_(item.xa_elem, {"copies": 2}, True)
        return self

    # Documents
    def documents(self, properties: Union[dict, None] = None) -> List['XAPagesDocument']:
        """Returns a list of documents, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned documents will have, or None
        :type filter: Union[dict, None]
        :return: The list of documents
        :rtype: List[XAPagesDocument]

        :Example 1: List all documents

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes())

        :Example 2: List documents after applying a filter

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes({"name": "Accessibility"}))

        .. versionadded:: 0.0.2
        """
        return super().scriptable_elements("documents", properties, XAPagesDocument)

    def document(self, properties: Union[int, dict]) -> 'XAPagesDocument':
        """Returns the first document matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned document will have
        :type filter: Union[int, dict]
        :return: The document
        :rtype: XAPagesDocument

        :Example 1: Get a document by index

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.pane(0))

        :Example 2: Get a document by using a filter

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes({"name": "Accessibility"}))

        .. versionadded:: 0.0.2
        """
        return super().scriptable_element_with_properties("documents", properties, XAPagesDocument)

    def first_document(self) -> 'XAPagesDocument':
        """Returns the document at the zero index of the documents array.

        :return: The first document
        :rtype: XAPagesDocument

        .. versionadded:: 0.0.2
        """
        return super().first_scriptable_element("documents", XAPagesDocument)

    def last_document(self) -> 'XAPagesDocument':
        """Returns the document at the last (-1) index of the documents array.

        :return: The last document
        :rtype: XAPagesDocument

        .. versionadded:: 0.0.2
        """
        return super().last_scriptable_element("documents", XAPagesDocument)

    def new_slide(self, document: 'XAPagesDocument', properties: dict):
        return self.push("slide", properties, document.xa_elem.slides())

    # Themes
    def themes(self, properties: Union[dict, None] = None) -> List['XAPagesTheme']:
        """Returns a list of themes, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned themes will have, or None
        :type filter: Union[dict, None]
        :return: The list of themes
        :rtype: List[XAPagesTheme]

        :Example 1: List all themes

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes())

        :Example 2: List themes after applying a filter

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes({"name": "Accessibility"}))

        .. versionadded:: 0.0.2
        """
        return super().scriptable_elements("themes", properties, XAPagesTheme)

    def theme(self, properties: Union[int, dict]) -> 'XAPagesTheme':
        """Returns the first theme matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned theme will have
        :type filter: Union[int, dict]
        :return: The theme
        :rtype: XAPagesTheme

        :Example 1: Get a theme by index

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.pane(0))

        :Example 2: Get a theme by using a filter

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes({"name": "Accessibility"}))

        .. versionadded:: 0.0.2
        """
        return super().scriptable_element_with_properties("themes", properties, XAPagesTheme)

    def first_theme(self) -> 'XAPagesTheme':
        """Returns the theme at the zero index of the themes array.

        :return: The first theme
        :rtype: XAPagesTheme

        .. versionadded:: 0.0.2
        """
        return super().first_scriptable_element("themes", XAPagesTheme)

    def last_theme(self) -> 'XAPagesTheme':
        """Returns the theme at the last (-1) index of the themes array.

        :return: The last theme
        :rtype: XAPagesTheme

        .. versionadded:: 0.0.2
        """
        return super().last_scriptable_element("themes", XAPagesTheme)

class XAPagesWindow(XABaseScriptable.XASBWindow, XABaseScriptable.XASBPrintable, XABase.XAHasElements):
    """A class for managing and interacting with windows in Keynote.app.

    .. versionadded:: 0.0.1
    """
    def __init__(self, properties):
        super().__init__(properties)
        
    @property
    def document(self) -> 'XAPagesDocument':
        if self.__document is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_scel.document(),
                "scriptable_element": self.xa_scel.document(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__column = XAPagesDocument(properties)
        return self.__document

class XAPagesDocument(XABase.XAHasElements, XABaseScriptable.XASBPrintable, XABaseScriptable.XASBCloseable, XABase.XAAcceptsPushedElements, XABase.XACanConstructElement):
    """A class for managing and interacting with TextEdit documents.

    .. seealso:: :class:`XAPagesApplication`

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.properties: dict = self.xa_elem.properties()
        self.name: str = self.xa_elem.name()
        self.modified: bool = self.xa_elem.modified()
        self.file: str = self.xa_elem.file()
        self.id: str = self.xa_elem.id()
        self.slide_numbers_showing: bool = self.xa_elem.slideNumbersShowing()
        self.auto_loop: bool = self.xa_elem.autoLoop()
        self.auto_play: bool = self.xa_elem.autoPlay()
        self.auto_restart: bool = self.xa_elem.autoRestart()
        self.maximum_idle_duration: int = self.xa_elem.maximumIdleDuration()
        self.height: int = self.xa_elem.height()
        self.width: int = self.xa_elem.width()
        self.password_protected: bool = self.xa_elem.passwordProtected()
        self.__document_theme: 'XAPagesTheme' = None
        self.__current_slide: 'XAPagesSlide' = None
        self.__selection: List['XAPagesiWorkItem'] = None

    @property
    def document_theme(self) -> 'XAPagesTheme':
        if self.__document_theme is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.documentTheme(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__document_theme = XAPagesTheme(properties)
        return self.__document_theme

    @property
    def current_slide(self) -> 'XAPagesSlide':
        if self.__current_slide is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.currentSlide(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__current_slide = XAPagesSlide(properties)
        return self.__current_slide

    @property
    def selection(self) -> 'XAPagesiWorkItem':
        if self.__selection is None:
            objects = []
            items = self.xa_elem.selection()
            for item in items:
                properties = {
                    "parent": self,
                    "appspace": self.xa_apsp,
                    "workspace": self.xa_wksp,
                    "element": item,
                    "appref": self.xa_aref,
                    "system_events": self.xa_sevt,
                }
                description = item.specifierDescription()
                element_class = XAPagesiWorkItem
                if "defaultBodyItem" in description or "defaultTitleItem" in description or "sshp" in description:
                    element_class = XAPagesShape
                elif "shtx" in description:
                    element_class = XAPagesTextItem
                elif "imag" in description:
                    element_class = XAPagesImage
                elif "igrp" in description:
                    element_class = XAPagesGroup
                elif 'iWln' in description:
                    element_class = XAPagesLine
                elif "NmTb" in description:
                    element_class = XAPagesTable
                elif "shau" in description:
                    element_class = XAPagesAudioClip
                elif "shmv" in description:
                    element_class = XAPagesMovie
                elif "shct" in description:
                    element_class = XAPagesChart
                objects.append(element_class(properties))
            self.__selection = objects
        return self.__selection

    def start_from(self, slide: 'XAPagesSlide') -> 'XAPagesSlide':
        self.xa_elem.startFrom_(slide.xa_elem)
        return self

    def stop(self):
        self.xa_elem.stop()

    def show_slide_switcher(self):
        self.xa_elem.showSlideSwitcher()

    def hide_slide_switcher(self):
        self.xa_elem.hideSlideSwitcher()

    def move_slide_switcher_forward(self):
        self.xa_elem.moveSlideSwitcherForward()

    def move_slide_switcher_backward(self):
        self.xa_elem.moveSlideSwitcherBackward()

    def cancel_slide_switcher(self):
        self.xa_elem.cancelSlideSwitcher()

    def accept_slide_switcher(self):
        self.xa_elem.acceptSlideSwitcher()

    def save(self, file_path: str = None, file_type: str = None):
        file_path = "/Users/steven/Downloads/Test.key"
        export_format = XAPagesApplication.ExportFormat.KEYNOTE.value
        url = NSURL.alloc().initFileURLWithPath_(file_path)
        # self.xa_elem.exportTo_as_withProperties_(url, export_format, None)
        self.xa_elem.saveIn_as_(url, export_format)

    def export(self, file_path: str = None, file_type: str = None):
        file_path = "/Users/steven/Downloads/wowwwwww.pdf"
        export_format = XAPagesApplication.ExportFormat.PDF.value
        url = NSURL.alloc().initFileURLWithPath_(file_path)
        self.xa_elem.exportTo_as_withProperties_(url, export_format, None)

    def make_image_slides(self, files: List[Union[str, NSURL]], set_titles: bool = False, slide_layout: 'XAPagesSlideLayout' = None) -> 'XAPagesDocument':
        urls = []
        for file in files:
            if isinstance(file, str):
                file = NSURL.alloc().initFileURLWithPath_(file)
            urls.append(file)
        self.xa_elem.makeImageSlidesFiles_setTitles_slideLayout_(urls, set_titles, slide_layout)
        return self

    # def save(self, file_path: str = None):
    #     # file_path = "/Users/steven/Documents/eek/wow"
    #     url = self.file
    #     if file_path is not None:
    #         url = NSURL.alloc().initFileURLWithPath_(file_path)
    #     self.xa_elem.saveIn_as_(url, _KeynoteSaveableFileFormat.KeynoteSaveableFileFormatKeynote.value)

    # Slides
    def slides(self, properties: Union[dict, None] = None) -> List['XAPagesSlide']:
        """Returns a list of slides, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned slides will have, or None
        :type filter: Union[dict, None]
        :return: The list of slides
        :rtype: List[XAPagesSlide]

        :Example 1: List all slides

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes())

        :Example 2: List slides after applying a filter

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes({"name": "Accessibility"}))

        .. versionadded:: 0.0.2
        """
        return super().elements("slides", properties, XAPagesSlide)

    def slide(self, properties: Union[int, dict]) -> 'XAPagesSlide':
        """Returns the first slide matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned slide will have
        :type filter: Union[int, dict]
        :return: The slide
        :rtype: XAPagesSlide

        :Example 1: Get a slide by index

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.pane(0))

        :Example 2: Get a slide by using a filter

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes({"name": "Accessibility"}))

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("slides", properties, XAPagesSlide)

    def first_slide(self) -> 'XAPagesSlide':
        """Returns the slide at the zero index of the slides array.

        :return: The first slide
        :rtype: XAPagesSlide

        .. versionadded:: 0.0.2
        """
        return super().first_element("slides", XAPagesSlide)

    def last_slide(self) -> 'XAPagesSlide':
        """Returns the slide at the last (-1) index of the slides array.

        :return: The last slide
        :rtype: XAPagesSlide

        .. versionadded:: 0.0.2
        """
        return super().last_element("slides", XAPagesSlide)

    def new_slide(self, properties: dict) -> 'XAPagesSlide':
        """Creates a new slide at the end of the presentation.

        :param properties: The properties to give the new slide
        :type properties: dict
        :return: A reference to the newly created slide
        :rtype: XAPagesSlide

        .. versionadded:: 0.0.2
        """
        return self.xa_prnt.new_slide(self, properties)

    # Slide Layouts
    def slide_layouts(self, properties: Union[dict, None] = None) -> List['XAPagesSlideLayout']:
        """Returns a list of slide_layouts, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned slide_layouts will have, or None
        :type filter: Union[dict, None]
        :return: The list of slide_layouts
        :rtype: List[XAPagesSlideLayout]

        :Example 1: List all slide_layouts

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes())

        :Example 2: List slide_layouts after applying a filter

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes({"name": "Accessibility"}))

        .. versionadded:: 0.0.2
        """
        return super().elements("slideLayouts", properties, XAPagesSlideLayout)

    def slide_layout(self, properties: Union[int, dict]) -> 'XAPagesSlideLayout':
        """Returns the first slide_layout matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned slide_layout will have
        :type filter: Union[int, dict]
        :return: The slide_layout
        :rtype: XAPagesSlideLayout

        :Example 1: Get a slide_layout by index

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.pane(0))

        :Example 2: Get a slide_layout by using a filter

        >>> import PyXA
        >>> app = PyXA.application("System Preferences")
        >>> print(app.panes({"name": "Accessibility"}))

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("slideLayouts", properties, XAPagesSlideLayout)

    def first_slide_layout(self) -> 'XAPagesSlideLayout':
        """Returns the slide_layout at the zero index of the slide_layouts array.

        :return: The first slide_layout
        :rtype: XAPagesSlideLayout

        .. versionadded:: 0.0.2
        """
        return super().first_element("slideLayouts", XAPagesSlideLayout)

    def last_slide_layout(self) -> 'XAPagesSlideLayout':
        """Returns the slide_layout at the last (-1) index of the slide_layouts array.

        :return: The last slide_layout
        :rtype: XAPagesSlideLayout

        .. versionadded:: 0.0.2
        """
        return super().last_element("slideLayouts", XAPagesSlideLayout)


class XAPagesTheme(XABaseScriptable.XASBObject):
    """A class for managing and interacting with Keynote themes.

    .. seealso:: :class:`XAPagesApplication`

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.id = self.xa_elem.id()
        self.name = self.xa_elem.name()

class XAPagesContainer(XABase.XAHasElements):
    """A class for managing and interacting with containers in Keynote.

    .. seealso:: :class:`XAPagesApplication`, :class:`XAPagesiWorkItem`

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)

    # iWork Items
    def iwork_items(self, properties: Union[dict, None] = None) -> List['XAPagesiWorkItem']:
        """Returns a list of iWork items, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned iWork items will have, or None
        :type filter: Union[dict, None]
        :return: The list of iWork items
        :rtype: List[XAPagesiWorkItem]

        .. versionadded:: 0.0.2
        """
        return super().elements("iWorkItems", properties, XAPagesiWorkItem)

    def iwork_item(self, properties: Union[int, dict]) -> 'XAPagesiWorkItem':
        """Returns the first iWork item matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned iWork item will have
        :type filter: Union[int, dict]
        :return: The iWork item
        :rtype: XAPagesiWorkItem

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("iWorkItems", properties, XAPagesiWorkItem)

    def first_iwork_item(self) -> 'XAPagesiWorkItem':
        """Returns the iWork item at the zero index of the iWork items array.

        :return: The first iWork item
        :rtype: XAPagesiWorkItem

        .. versionadded:: 0.0.2
        """
        return super().first_element("iWorkItems", XAPagesiWorkItem)

    def last_iwork_item(self) -> 'XAPagesiWorkItem':
        """Returns the iWork item at the last (-1) index of the iWork items array.

        :return: The last iWork item
        :rtype: XAPagesiWorkItem

        .. versionadded:: 0.0.2
        """
        return super().last_element("iWorkItems", XAPagesiWorkItem)

    # AudioClips
    def audio_clips(self, properties: Union[dict, None] = None) -> List['XAPagesAudioClip']:
        """Returns a list of audio clips, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned audio clips will have, or None
        :type filter: Union[dict, None]
        :return: The list of audio clips
        :rtype: List[XAPagesAudioClip]

        .. versionadded:: 0.0.2
        """
        return super().elements("audioClips", properties, XAPagesAudioClip)

    def audio_clip(self, properties: Union[int, dict]) -> 'XAPagesAudioClip':
        """Returns the first image matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned audio clip will have
        :type filter: Union[int, dict]
        :return: The audio clip
        :rtype: XAPagesAudioClip

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("audioClips", properties, XAPagesAudioClip)

    def first_audio_clip(self) -> 'XAPagesAudioClip':
        """Returns the audio clip at the zero index of the audio clips array.

        :return: The first image
        :rtype: XAPagesAudioClip

        .. versionadded:: 0.0.2
        """
        return super().first_element("audioClips", XAPagesAudioClip)

    def last_audio_clip(self) -> 'XAPagesAudioClip':
        """Returns the audio clip at the last (-1) index of the audio clips array.

        :return: The last audio clip
        :rtype: XAPagesAudioClip

        .. versionadded:: 0.0.2
        """
        return super().last_element("audioClips", XAPagesAudioClip)

    # Charts
    def charts(self, properties: Union[dict, None] = None) -> List['XAPagesChart']:
        """Returns a list of charts, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned charts will have, or None
        :type filter: Union[dict, None]
        :return: The list of charts
        :rtype: List[XAPagesChart]

        .. versionadded:: 0.0.2
        """
        return super().elements("charts", properties, XAPagesChart)

    def chart(self, properties: Union[int, dict]) -> 'XAPagesChart':
        """Returns the first image matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned chart will have
        :type filter: Union[int, dict]
        :return: The chart
        :rtype: XAPagesChart

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("charts", properties, XAPagesChart)

    def first_chart(self) -> 'XAPagesChart':
        """Returns the chart at the zero index of the charts array.

        :return: The first image
        :rtype: XAPagesChart

        .. versionadded:: 0.0.2
        """
        return super().first_element("charts", XAPagesChart)

    def last_chart(self) -> 'XAPagesChart':
        """Returns the chart at the last (-1) index of the charts array.

        :return: The last chart
        :rtype: XAPagesChart

        .. versionadded:: 0.0.2
        """
        return super().last_element("charts", XAPagesChart)

    # Images
    def images(self, properties: Union[dict, None] = None) -> List['XAPagesImage']:
        """Returns a list of images, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned images will have, or None
        :type filter: Union[dict, None]
        :return: The list of images
        :rtype: List[XAPagesImage]

        .. versionadded:: 0.0.2
        """
        return super().elements("images", properties, XAPagesImage)

    def image(self, properties: Union[int, dict]) -> 'XAPagesImage':
        """Returns the first image matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned image will have
        :type filter: Union[int, dict]
        :return: The image
        :rtype: XAPagesImage

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("images", properties, XAPagesImage)

    def first_image(self) -> 'XAPagesImage':
        """Returns the image at the zero index of the images array.

        :return: The first image
        :rtype: XAPagesImage

        .. versionadded:: 0.0.2
        """
        return super().first_element("images", XAPagesImage)

    def last_image(self) -> 'XAPagesImage':
        """Returns the image at the last (-1) index of the images array.

        :return: The last image
        :rtype: XAPagesImage

        .. versionadded:: 0.0.2
        """
        return super().last_element("images", XAPagesImage)

    # Groups
    def groups(self, properties: Union[dict, None] = None) -> List['XAPagesGroup']:
        """Returns a list of groups, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned groups will have, or None
        :type filter: Union[dict, None]
        :return: The list of groups
        :rtype: List[XAPagesGroup]

        .. versionadded:: 0.0.2
        """
        return super().elements("groups", properties, XAPagesGroup)

    def group(self, properties: Union[int, dict]) -> 'XAPagesGroup':
        """Returns the first group matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned group will have
        :type filter: Union[int, dict]
        :return: The group
        :rtype: XAPagesGroup

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("groups", properties, XAPagesGroup)

    def first_group(self) -> 'XAPagesGroup':
        """Returns the group at the zero index of the groups array.

        :return: The first group
        :rtype: XAPagesGroup

        .. versionadded:: 0.0.2
        """
        return super().first_element("groups", XAPagesGroup)

    def last_group(self) -> 'XAPagesGroup':
        """Returns the group at the last (-1) index of the groups array.

        :return: The last group
        :rtype: XAPagesGroup

        .. versionadded:: 0.0.2
        """
        return super().last_element("groups", XAPagesGroup)

    # Lines
    def lines(self, properties: Union[dict, None] = None) -> List['XAPagesLine']:
        """Returns a list of lines, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned lines will have, or None
        :type filter: Union[dict, None]
        :return: The list of lines
        :rtype: List[XAPagesLine]

        .. versionadded:: 0.0.2
        """
        return super().elements("lines", properties, XAPagesLine)

    def line(self, properties: Union[int, dict]) -> 'XAPagesLine':
        """Returns the first line matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned line will have
        :type filter: Union[int, dict]
        :return: The line
        :rtype: XAPagesLine

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("lines", properties, XAPagesLine)

    def first_line(self) -> 'XAPagesLine':
        """Returns the line at the zero index of the lines array.

        :return: The first line
        :rtype: XAPagesLine

        .. versionadded:: 0.0.2
        """
        return super().first_element("lines", XAPagesLine)

    def last_line(self) -> 'XAPagesLine':
        """Returns the line at the last (-1) index of the lines array.

        :return: The last line
        :rtype: XAPagesLine

        .. versionadded:: 0.0.2
        """
        return super().last_element("lines", XAPagesLine)

    # Movies
    def movies(self, properties: Union[dict, None] = None) -> List['XAPagesMovie']:
        """Returns a list of movies, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned movies will have, or None
        :type filter: Union[dict, None]
        :return: The list of movies
        :rtype: List[XAPagesMovie]

        .. versionadded:: 0.0.2
        """
        return super().elements("movies", properties, XAPagesMovie)

    def movie(self, properties: Union[int, dict]) -> 'XAPagesMovie':
        """Returns the first movie matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned movie will have
        :type filter: Union[int, dict]
        :return: The movie
        :rtype: XAPagesMovie

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("movies", properties, XAPagesMovie)

    def first_movie(self) -> 'XAPagesMovie':
        """Returns the movie at the zero index of the movies array.

        :return: The first movie
        :rtype: XAPagesMovie

        .. versionadded:: 0.0.2
        """
        return super().first_element("movies", XAPagesMovie)

    def last_movie(self) -> 'XAPagesMovie':
        """Returns the movie at the last (-1) index of the movies array.

        :return: The last movie
        :rtype: XAPagesMovie

        .. versionadded:: 0.0.2
        """
        return super().last_element("movies", XAPagesMovie)

    # Shapes
    def shapes(self, properties: Union[dict, None] = None) -> List['XAPagesShape']:
        """Returns a list of shapes, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned shapes will have, or None
        :type filter: Union[dict, None]
        :return: The list of shapes
        :rtype: List[XAPagesShape]

        .. versionadded:: 0.0.2
        """
        return super().elements("shapes", properties, XAPagesShape)

    def shape(self, properties: Union[int, dict]) -> 'XAPagesShape':
        """Returns the first shape matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned shape will have
        :type filter: Union[int, dict]
        :return: The shape
        :rtype: XAPagesShape

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("shapes", properties, XAPagesShape)

    def first_shape(self) -> 'XAPagesShape':
        """Returns the shape at the zero index of the shapes array.

        :return: The first shape
        :rtype: XAPagesShape

        .. versionadded:: 0.0.2
        """
        return super().first_element("shapes", XAPagesShape)

    def last_shape(self) -> 'XAPagesShape':
        """Returns the shape at the last (-1) index of the shapes array.

        :return: The last shape
        :rtype: XAPagesShape

        .. versionadded:: 0.0.2
        """
        return super().last_element("shapes", XAPagesShape)

    # Tables
    def tables(self, properties: Union[dict, None] = None) -> List['XAPagesTable']:
        """Returns a list of tables, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned tables will have, or None
        :type filter: Union[dict, None]
        :return: The list of tables
        :rtype: List[XAPagesTable]

        .. versionadded:: 0.0.2
        """
        return super().elements("tables", properties, XAPagesTable)

    def table(self, properties: Union[int, dict]) -> 'XAPagesTable':
        """Returns the first table matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned table will have
        :type filter: Union[int, dict]
        :return: The table
        :rtype: XAPagesTable

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("tables", properties, XAPagesTable)

    def first_table(self) -> 'XAPagesTable':
        """Returns the table at the zero index of the tables array.

        :return: The first table
        :rtype: XAPagesTable

        .. versionadded:: 0.0.2
        """
        return super().first_element("tables", XAPagesTable)

    def last_table(self) -> 'XAPagesTable':
        """Returns the table at the last (-1) index of the tables array.

        :return: The last table
        :rtype: XAPagesTable

        .. versionadded:: 0.0.2
        """
        return super().last_element("tables", XAPagesTable)

    # Text Items
    def text_items(self, properties: Union[dict, None] = None) -> List['XAPagesTextItem']:
        """Returns a list of text_items, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned text_items will have, or None
        :type filter: Union[dict, None]
        :return: The list of text_items
        :rtype: List[XAPagesTextItem]

        .. versionadded:: 0.0.2
        """
        return super().elements("text_items", properties, XAPagesTextItem)

    def text_item(self, properties: Union[int, dict]) -> 'XAPagesTextItem':
        """Returns the first text_item matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned text_item will have
        :type filter: Union[int, dict]
        :return: The text_item
        :rtype: XAPagesTextItem

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("text_items", properties, XAPagesTextItem)

    def first_text_item(self) -> 'XAPagesTextItem':
        """Returns the text_item at the zero index of the text_items array.

        :return: The first text_item
        :rtype: XAPagesTextItem

        .. versionadded:: 0.0.2
        """
        return super().first_element("text_items", XAPagesTextItem)

    def last_text_item(self) -> 'XAPagesTextItem':
        """Returns the text_item at the last (-1) index of the text_items array.

        :return: The last text_item
        :rtype: XAPagesTextItem

        .. versionadded:: 0.0.2
        """
        return super().last_element("text_items", XAPagesTextItem)

class XAPagesSlide(XAPagesContainer):
    """A class for managing and interacting with TextEdit documents.

    .. seealso:: :class:`XAPagesApplication`, :class:`XAPagesiWorkItem`

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.properties: dict = self.xa_elem.properties()
        self.body_showing: bool = self.properties["bodyShowing"]
        self.skipped: bool = self.properties["skipped"]
        self.slide_number: int = self.properties["slideNumber"]
        self.title_showing: bool = self.properties["titleShowing"]
        self.transition_properties: dict = self.properties["transitionProperties"]
        self.__base_layout = None
        self.__default_body_item = None
        self.__default_title_item = None
        self.__presenter_notes = None

    @property
    def base_layout(self) -> 'XAPagesSlideLayout':
        if self.__base_layout is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.baseLayout(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__base_layout = XAPagesSlideLayout(properties)
        return self.__base_layout

    @property
    def default_body_item(self) -> 'XAPagesSlideLayout':
        if self.__default_body_item is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.defaultBodyItem(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__default_body_item = XAPagesShape(properties)
        return self.__default_body_item

    @property
    def default_title_item(self) -> 'XAPagesSlideLayout':
        if self.__default_title_item is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.defaultTitleItem(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__default_title_item = XAPagesShape(properties)
        return self.__default_title_item

    @property
    def presenter_notes(self) -> 'XAPagesSlideLayout':
        if self.__presenter_notes is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.presenterNotes(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__presenter_notes = XABase.XAText(properties)
        return self.__presenter_notes

    def duplicate(self) -> 'XAPagesSlide':
        """Duplicates the slide, mimicking the action of copying and pasting the slide manually.

        :return: A reference to the PyXA slide object that called this command.
        :rtype: XAPagesSlide

        .. versionadded:: 0.0.2
        """
        self.xa_elem.duplicateTo_withProperties_(self.xa_elem.positionAfter(), None)
        return self

    def delete(self):
        """Deletes the slide.

        .. versionadded:: 0.0.2
        """
        self.xa_elem.delete()

    def add_image(self, file_path: Union[str, NSURL]) -> 'XAPagesImage':
        """Adds the image at the specified path to the slide.

        :param file_path: The path to the image file.
        :type file_path: Union[str, NSURL]
        :return: The newly created image object.
        :rtype: XAPagesImage

        .. versionadded:: 0.0.2
        """
        url = file_path
        if isinstance(url, str):
            url = NSURL.alloc().initFileURLWithPath_(file_path)
        image = self.xa_prnt.xa_prnt.construct("image", {
            "file": url,
        })
        self.xa_elem.images().addObject_(image)
        properties = {
            "parent": self,
            "appspace": self.xa_apsp,
            "workspace": self.xa_wksp,
            "element": image,
            "appref": self.xa_aref,
            "system_events": self.xa_sevt,
        }
        return XAPagesImage(properties)

    def add_chart(self, row_names: List[str], column_names: List[str], data: List[List[Any]], type: int = XAPagesApplication.ChartType.LINE_2D.value, group_by: int = XAPagesApplication.ChartGrouping.ROW.value) -> 'XAPagesChart':
        """_summary_

        _extended_summary_

        :param row_names: A list of row names.
        :type row_names: List[str]
        :param column_names: A list of column names.
        :type column_names: List[str]
        :param data: A 2d array 
        :type data: List[List[Any]]
        :param type: The chart type, defaults to _KeynoteLegacyChartType.KeynoteLegacyChartTypeLine_2d.value
        :type type: int, optional
        :param group_by: The grouping schema, defaults to _KeynoteLegacyChartGrouping.KeynoteLegacyChartGroupingChartRow.value
        :type group_by: int, optional
        :return: A reference to the newly created chart object.
        :rtype: XAPagesChart

        .. versionadded:: 0.0.2
        """
        self.xa_prnt.set_property("currentSlide", self.xa_elem)
        self.xa_elem.addChartRowNames_columnNames_data_type_groupBy_(row_names, column_names, data, type, group_by)
        chart = self.xa_elem.charts()[-1].get()
        properties = {
            "parent": self,
            "appspace": self.xa_apsp,
            "workspace": self.xa_wksp,
            "element": chart,
            "appref": self.xa_aref,
            "system_events": self.xa_sevt,
        }
        return XAPagesChart(properties)


class XAPagesSlideLayout(XAPagesSlide):
    """A class for managing and interacting with TextEdit documents.

    .. seealso:: :class:`XAPagesSlide`

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.name = self.xa_elem.name()


class XAPagesiWorkItem(XABase.XAObject):
    """A class for managing and interacting with text, shapes, images, and other elements in Keynote.

    .. seealso:: :class:`XAPagesApplication`

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.height: int = self.xa_elem.height()
        self.locked: bool = self.xa_elem.locked()
        self.width: int = self.xa_elem.width()
        self.position: Tuple[int, int] = self.xa_elem.position()
        self.__parent = None

    @property
    def parent(self):
        if self.__parent == None:
            self.__parent = self.xa_prnt
        return self.__parent

    def delete(self):
        """Deletes the item.

        .. versionadded:: 0.0.2
        """
        self.xa_elem.delete()

    def duplicate(self) -> 'XAPagesiWorkItem':
        """Duplicates the item.

        :return: A reference to the PyXA object that called this method.
        :rtype: XAPagesiWorkItem

        .. versionadded:: 0.0.2
        """
        self.xa_elem.duplicateTo_withProperties_(self.xa_prnt.xa_elem.iWorkItems(), None)
        return self

    def resize(self, width: int, height: int) -> 'XAPagesiWorkItem':
        """Sets the width and height of the item.

        :param width: The desired width, in pixels
        :type width: int
        :param height: The desired height, in pixels
        :type height: int
        :return: The iWork item
        :rtype: XAPagesiWorkItem

        .. versionadded:: 0.0.2
        """
        self.set_properties({
            "width": width,
            "height": height,
        })
        return self

    def lock(self) -> 'XAPagesiWorkItem':
        """Locks the properties of the item, preventing changes.

        :return: The iWork item
        :rtype: XAPagesiWorkItem

        .. versionadded:: 0.0.2
        """
        self.set_property("locked", True)
        return self

    def unlock(self) -> 'XAPagesiWorkItem':
        """Unlocks the properties of the item, allowing changes.

        :return: The iWork item
        :rtype: XAPagesiWorkItem

        .. versionadded:: 0.0.2
        """
        self.set_property("locked", False)
        return self

    def set_position(self, x: int, y: int) -> 'XAPagesiWorkItem':
        position = NSValue.valueWithPoint_(NSPoint(x, y))
        self.xa_elem.setValue_forKey_(position, "position")

class XAPagesGroup(XAPagesContainer):
    """A class for managing and interacting with iWork item groups in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.height: int = self.xa_elem.height()
        self.position: Tuple[int, int] = self.xa_elem.position()
        self.width: int = self.xa_elem.width()
        self.rotation: int = self.xa_elem.rotation()
        self.__parent = None

    @property
    def parent(self):
        if self.__parent == None:
            self.__parent = self.xa_prnt
        return self.__parent

class XAPagesImage(XAPagesiWorkItem):
    """A class for managing and interacting with images in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.description: str = self.xa_elem.objectDescription()
        self.file = self.xa_elem.file()
        self.file_name: str = self.xa_elem.fileName().get()
        self.opacity: int = self.xa_elem.opacity()
        self.reflection_showing: bool = self.xa_elem.reflectionShowing()
        self.reflection_value: int = self.xa_elem.reflectionValue()
        self.rotation: int = self.xa_elem.rotation()

    def rotate(self, degrees: int) -> 'XAPagesImage':
        """Rotates the image by the specified number of degrees.

        :param degrees: The amount to rotate the image, in degrees, from -359 to 359
        :type degrees: int
        :return: The image.
        :rtype: XAPagesImage

        .. versionadded:: 0.0.2
        """
        self.set_property("rotation", self.rotation + degrees)
        return self

    def replace_with(self, img_path: Union[str, NSURL]) -> 'XAPagesImage':
        """Removes the image and inserts another in its place with the same width and height.

        :param img_path: The path to the new image file.
        :type img_path: Union[str, NSURL]
        :return: A reference to the new PyXA image object.
        :rtype: XAPagesImage

        .. versionadded:: 0.0.2
        """
        self.delete()
        return self.xa_prnt.add_image(img_path)

class XAPagesAudioClip(XAPagesiWorkItem):
    """A class for managing and interacting with audio clips in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.file_name: str = self.xa_elem.fileName()
        self.clip_volume: int = self.xa_elem.clipVolume()
        self.repitition_method: int = self.xa_elem.repetitionMethod()

class XAPagesShape(XAPagesiWorkItem):
    """A class for managing and interacting with shapes in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.background_fill_type: int = self.xa_elem.backgroundFillType()
        self.text: str = self.xa_elem.objectText()
        self.opacity: int = self.xa_elem.opacity()
        self.reflection_showing: bool = self.xa_elem.reflectionShowing()
        self.reflection_value: int = self.xa_elem.reflectionValue()
        self.rotation: int = self.xa_elem.rotation()

    def rotate(self, degrees: int) -> 'XAPagesShape':
        """Rotates the shape by the specified number of degrees.

        :param degrees: The amount to rotate the shape, in degrees, from -359 to 359
        :type degrees: int
        :return: The shape.
        :rtype: XAPagesShape

        .. versionadded:: 0.0.2
        """
        self.set_property("rotation", self.rotation + degrees)
        return self

class XAPagesChart(XAPagesiWorkItem):
    """A class for managing and interacting with charts in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)

class XAPagesLine(XAPagesiWorkItem):
    """A class for managing and interacting with lines in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.end_point: Tuple[int, int] = self.xa_elem.endPoint()
        self.reflection_showing: bool = self.xa_elem.reflectionShowing()
        self.reflection_value: int = self.xa_elem.reflectionValue()
        self.rotation: int = self.xa_elem.rotation()
        self.start_point: Tuple[int, int] = self.xa_elem.startPoint()

class XAPagesMovie(XAPagesiWorkItem):
    """A class for managing and interacting with movie containers in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.file_name: str = self.xa_elem.fileName()
        self.movie_volume: int = self.xa_elem.movieVolume()
        self.opacity: int = self.xa_elem.opacity()
        self.reflection_showing: bool = self.xa_elem.reflectionShowing()
        self.reflection_value: int = self.xa_elem.reflectionValue()
        self.repetition_method: int = self.xa_elem.repetitionMethod()
        self.rotation: int = self.xa_elem.rotation()

class XAPagesTextItem(XAPagesiWorkItem):
    """A class for managing and interacting with text items in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.background_fill_type: int = self.xa_elem.backgroundFillType()
        self.text = XABase.XAText(self.xa_elem.objectText().properties())
        print(self.text)
        self.opacity: int = self.xa_elem.opacity()
        self.reflection_showing: bool = self.xa_elem.reflectionShowing()
        self.reflection_value: int = self.xa_elem.reflectionValue()
        self.rotation: int = self.xa_elem.rotation()

class XAPagesTable(XAPagesiWorkItem, XABase.XAHasElements):
    """A class for managing and interacting with tables in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.name: str = self.xa_elem.name() #: The name of the table
        self.row_count: int = self.xa_elem.rowCount() #: The number of rows in the table
        self.column_count: int = self.xa_elem.columnCount() #: The number of columns in the table
        self.header_row_count: int = self.xa_elem.headerRowCount() #: The number of header rows in the table
        self.header_column_count: int = self.xa_elem.headerColumnCount() #: The number of header columns in the table
        self.footer_row_count: int = self.xa_elem.footerRowCount() #: The number of footer rows in the table
        self.__cell_range = None #: The range of all cells in the table
        self.__selection_range = None #: The currently selected cells

    @property
    def cell_range(self) -> 'XAPagesRange':
        if self.__cell_range is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.cellRange(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__cell_range = XAPagesRange(properties)
        return self.__cell_range

    @property
    def selection_range(self) -> 'XAPagesRange':
        if self.__selection_range is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.selectionRange(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__selection_range = XAPagesRange(properties)
        return self.__selection_range

    # TODO
    def sort(self, columns: List['XAPagesColumn'], rows: List['XAPagesRow'], direction: XAPagesApplication.SortDirection = XAPagesApplication.SortDirection.ASCENDING) -> 'XAPagesTable':
        column_objs = [column.xa_elem for column in columns]
        row_objs = [row.xa_elem for row in rows]
        self.xa_elem.sortBy_direction_inRows_(column_objs[0], direction.value, row_objs)
        return self

    # Cells
    def cells(self, properties: Union[dict, None] = None) -> List['XAPagesCell']:
        """Returns a list of cells, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned cells will have, or None
        :type filter: Union[dict, None]
        :return: The list of cells
        :rtype: List[XAPagesCell]

        .. versionadded:: 0.0.2
        """
        return super().elements("cells", properties, XAPagesCell)

    def cell(self, properties: Union[int, dict]) -> 'XAPagesCell':
        """Returns the first cell matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned cell will have
        :type filter: Union[int, dict]
        :return: The cell
        :rtype: XAPagesCell

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("cells", properties, XAPagesCell)

    def first_cell(self) -> 'XAPagesCell':
        """Returns the cell at the zero index of the cells array.

        :return: The first cell
        :rtype: XAPagesCell

        .. versionadded:: 0.0.2
        """
        return super().first_element("cells", XAPagesCell)

    def last_cell(self) -> 'XAPagesCell':
        """Returns the cell at the last (-1) index of the cells array.

        :return: The last cell
        :rtype: XAPagesCell

        .. versionadded:: 0.0.2
        """
        return super().last_element("cells", XAPagesCell)

    # Columns
    def columns(self, properties: Union[dict, None] = None) -> List['XAPagesColumn']:
        """Returns a list of columns, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned columns will have, or None
        :type filter: Union[dict, None]
        :return: The list of columns
        :rtype: List[XAPagesColumn]

        .. versionadded:: 0.0.2
        """
        return super().elements("columns", properties, XAPagesColumn)

    def column(self, properties: Union[int, dict]) -> 'XAPagesColumn':
        """Returns the first column matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned column will have
        :type filter: Union[int, dict]
        :return: The column
        :rtype: XAPagesColumn

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("columns", properties, XAPagesColumn)

    def first_column(self) -> 'XAPagesColumn':
        """Returns the column at the zero index of the columns array.

        :return: The first column
        :rtype: XAPagesColumn

        .. versionadded:: 0.0.2
        """
        return super().first_element("columns", XAPagesColumn)

    def last_column(self) -> 'XAPagesColumn':
        """Returns the column at the last (-1) index of the columns array.

        :return: The last column
        :rtype: XAPagesColumn

        .. versionadded:: 0.0.2
        """
        return super().last_element("columns", XAPagesColumn)

    # Rows
    def rows(self, properties: Union[dict, None] = None) -> List['XAPagesRow']:
        """Returns a list of rows, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned rows will have, or None
        :type filter: Union[dict, None]
        :return: The list of rows
        :rtype: List[XAPagesRow]

        .. versionadded:: 0.0.2
        """
        return super().elements("rows", properties, XAPagesRow)

    def row(self, properties: Union[int, dict]) -> 'XAPagesRow':
        """Returns the first row matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned row will have
        :type filter: Union[int, dict]
        :return: The row
        :rtype: XAPagesRow

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("rows", properties, XAPagesRow)

    def first_row(self) -> 'XAPagesRow':
        """Returns the row at the zero index of the rows array.

        :return: The first row
        :rtype: XAPagesRow

        .. versionadded:: 0.0.2
        """
        return super().first_element("rows", XAPagesRow)

    def last_row(self) -> 'XAPagesRow':
        """Returns the row at the last (-1) index of the rows array.

        :return: The last row
        :rtype: XAPagesRow

        .. versionadded:: 0.0.2
        """
        return super().last_element("rows", XAPagesRow)

    # Ranges
    def ranges(self, properties: Union[dict, None] = None) -> List['XAPagesRange']:
        """Returns a list of ranges, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned ranges will have, or None
        :type filter: Union[dict, None]
        :return: The list of ranges
        :rtype: List[XAPagesRange]

        .. versionadded:: 0.0.2
        """
        return super().elements("ranges", properties, XAPagesRange)

    def range(self, properties: Union[int, dict]) -> 'XAPagesRange':
        """Returns the first range matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned range will have
        :type filter: Union[int, dict]
        :return: The range
        :rtype: XAPagesRange

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("ranges", properties, XAPagesRange)

    def first_range(self) -> 'XAPagesRange':
        """Returns the range at the zero index of the ranges array.

        :return: The first range
        :rtype: XAPagesRange

        .. versionadded:: 0.0.2
        """
        return super().first_element("ranges", XAPagesRange)

    def last_range(self) -> 'XAPagesRange':
        """Returns the range at the last (-1) index of the ranges array.

        :return: The last range
        :rtype: XAPagesRange

        .. versionadded:: 0.0.2
        """
        return super().last_element("ranges", XAPagesRange)

class XAPagesRange(XABase.XAHasElements):
    """A class for managing and interacting with ranges of table cells in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.properties = self.xa_elem.properties()
        self.font_name: str = self.xa_elem.fontName()
        self.font_size: float = self.xa_elem.fontSize()
        self.format: int = self.xa_elem.format()
        self.alignment: int = self.xa_elem.alignment()
        self.name: str = self.xa_elem.name()
        self.text_wrap: bool = self.xa_elem.textWrap()
        self.vertical_alignment: int = self.xa_elem.verticalAlignment()
        self.__text_color = None
        self.__background_color = None

    @property
    def text_color(self) -> XABase.XAColor:
        if self.__text_color == None:
            color_obj = self.xa_elem.textColor()
            if color_obj is not None:
                self.__text_color = XABase.XAColor().copy_color(color_obj)
        return self.__text_color

    @property
    def background_color(self) -> XABase.XAColor:
        if self.__background_color == None:
            color_obj = self.xa_elem.backgroundColor()
            if color_obj is not None:
                self.__background_color = XABase.XAColor().copy_color(color_obj)
        return self.__background_color

    def clear(self) -> 'XAPagesRange':
        self.xa_elem.clear()
        return self

    def merge(self) -> 'XAPagesRange':
        self.xa_elem.merge()
        return self

    def unmerge(self) -> 'XAPagesRange':
        self.xa_elem.unmerge()
        return self

    # Cells
    def cells(self, properties: Union[dict, None] = None) -> List['XAPagesCell']:
        """Returns a list of cells, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned cells will have, or None
        :type filter: Union[dict, None]
        :return: The list of cells
        :rtype: List[XAPagesCell]

        .. versionadded:: 0.0.2
        """
        return super().elements("cells", properties, XAPagesCell)

    def cell(self, properties: Union[int, dict]) -> 'XAPagesCell':
        """Returns the first cell matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned cell will have
        :type filter: Union[int, dict]
        :return: The cell
        :rtype: XAPagesCell

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("cells", properties, XAPagesCell)

    def first_cell(self) -> 'XAPagesCell':
        """Returns the cell at the zero index of the cells array.

        :return: The first cell
        :rtype: XAPagesCell

        .. versionadded:: 0.0.2
        """
        return super().first_element("cells", XAPagesCell)

    def last_cell(self) -> 'XAPagesCell':
        """Returns the cell at the last (-1) index of the cells array.

        :return: The last cell
        :rtype: XAPagesCell

        .. versionadded:: 0.0.2
        """
        return super().last_element("cells", XAPagesCell)

    # Columns
    def columns(self, properties: Union[dict, None] = None) -> List['XAPagesColumn']:
        """Returns a list of columns, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned columns will have, or None
        :type filter: Union[dict, None]
        :return: The list of columns
        :rtype: List[XAPagesColumn]

        .. versionadded:: 0.0.2
        """
        return super().elements("columns", properties, XAPagesColumn)

    def column(self, properties: Union[int, dict]) -> 'XAPagesColumn':
        """Returns the first column matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned column will have
        :type filter: Union[int, dict]
        :return: The column
        :rtype: XAPagesColumn

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("columns", properties, XAPagesColumn)

    def first_column(self) -> 'XAPagesColumn':
        """Returns the column at the zero index of the columns array.

        :return: The first column
        :rtype: XAPagesColumn

        .. versionadded:: 0.0.2
        """
        return super().first_element("columns", XAPagesColumn)

    def last_column(self) -> 'XAPagesColumn':
        """Returns the column at the last (-1) index of the columns array.

        :return: The last column
        :rtype: XAPagesColumn

        .. versionadded:: 0.0.2
        """
        return super().last_element("columns", XAPagesColumn)

    # Rows
    def rows(self, properties: Union[dict, None] = None) -> List['XAPagesRow']:
        """Returns a list of rows, as PyXA objects, matching the given filter.

        :param filter: A dictionary specifying property-value pairs that all returned rows will have, or None
        :type filter: Union[dict, None]
        :return: The list of rows
        :rtype: List[XAPagesRow]

        .. versionadded:: 0.0.2
        """
        return super().elements("rows", properties, XAPagesRow)

    def row(self, properties: Union[int, dict]) -> 'XAPagesRow':
        """Returns the first row matching the given filter.

        :param filter: Either an array index or a dictionary specifying property-value pairs that the returned row will have
        :type filter: Union[int, dict]
        :return: The row
        :rtype: XAPagesRow

        .. versionadded:: 0.0.2
        """
        return super().element_with_properties("rows", properties, XAPagesRow)

    def first_row(self) -> 'XAPagesRow':
        """Returns the row at the zero index of the rows array.

        :return: The first row
        :rtype: XAPagesRow

        .. versionadded:: 0.0.2
        """
        return super().first_element("rows", XAPagesRow)

    def last_row(self) -> 'XAPagesRow':
        """Returns the row at the last (-1) index of the rows array.

        :return: The last row
        :rtype: XAPagesRow

        .. versionadded:: 0.0.2
        """
        return super().last_element("rows", XAPagesRow)

class XAPagesRow(XAPagesRange):
    """A class for managing and interacting with table rows in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.address: int = self.xa_elem.address() #: The index of the row in the table
        self.height: float = self.xa_elem.height() #: The height of the row in pixels

class XAPagesColumn(XAPagesRange):
    """A class for managing and interacting with table columns in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.address: int = self.xa_elem.address() #: The index of the column in the tabel
        self.width: float = self.xa_elem.width() #: The width of the column in pixels

class XAPagesCell(XAPagesRange):
    """A class for managing and interacting with table cells in Keynote.

    .. versionadded:: 0.0.2
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.formatted_value: str = self.xa_elem.formattedValue() #: The formatted form of the value stored in the cell
        self.formula: str = self.xa_elem.formula() #: The formula in the cell as text
        self.value = self.xa_elem.value() #: The value stored in the cell
        self.__column: XAPagesColumn = None #: The cell's column
        self.__row: XAPagesRow = None #: The cell's row

    @property
    def column(self) -> XAPagesColumn:
        if self.__column is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.column(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__column = XAPagesColumn(properties)
        return self.__column

    @property
    def row(self) -> XAPagesRow:
        if self.__row is None:
            properties = {
                "parent": self,
                "appspace": self.xa_apsp,
                "workspace": self.xa_wksp,
                "element": self.xa_elem.row(),
                "appref": self.xa_aref,
                "system_events": self.xa_sevt,
            }
            self.__row = XAPagesRow(properties)
        return self.__row