# -
# 
# Stubs generated using https://github.com/tomaszkurgan/dcc_generate_stubs
# 
# -

def aaf2fcp(deleteFile, dstPath, getFileName, progress, srcFile, terminate, waitCompletion):
    """
    aaf2fcp is undoable

    Args:
        deleteFile (boolean):  <C> Delete temporary file. Can only be used with the terminate option
        dstPath (string):  <C> Specifiy a destination path
        getFileName (int):  <C> Query output file name
        progress (int):  <C> Request progress report
        srcFile (string):  <C> Specifiy a source file
        terminate (int):  <C> Complete the task
        waitCompletion (int):  <C> Wait for the conversion process to complete
    Documentation:
        http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/aaf2fcp.html
    Examples:
        - import maya.cmds as cmds
        - 
        - 
        - handle = cmds.aaf2fcp(srcFile='c:/tmp/test.aaf', dstPath='c:/tmp')
        - destinationFile = cmds.aff2fcp(getFileName=handle)
        - cmds.aaf2fcp(waitCompletion=handle)
        - cmds.aaf2fcp(terminate=handle,deleteFile=False)
    """

def about(apiVersion, application, batch, buildDirectory, buildVariant, codeset,
          compositingManager, connected, ctime, currentDate, currentTime, cutIdentifier,
          date, environmentFile, evalVersion, file, fontInfo, helpDataDirectory,
          installedVersion, irix, is64, languageResources, linux, linux64, liveUpdate,
          localizedResourceLocation, ltVersion, macOS, macOSppc, macOSx86, ntOS,
          operatingSystem, operatingSystemVersion, preferences, product, qtVersion,
          tablet, tabletMode, uiLanguage, uiLanguageForStartup, uiLanguageIsLocalized,
          uiLocaleLanguage, version, win64, windowManager, windows):
    """
    about is NOT undoable

    Args:
        apiVersion (boolean):  <C> Returns the api version.
        application (boolean):  <C> Returns the application name string.
        batch (boolean):  <C> Returns true if application is in batch mode.
        buildDirectory (boolean):  <C> Returns the build directory string.
        buildVariant (boolean):  <C> Returns the build variant string.
        codeset (boolean):  <C> Returns a string identifying the codeset (codepage) of the locale that Maya is running in. Example return values include "UTF-8", "ISO-8859-1", "1252". Note that the codeset values and naming conventions are highly platform dependent.  They may differ in format even if they have the same meaning (e.g. "utf8" vs. "UTF-8").
        compositingManager (boolean):  <C> On Linux, returns true if there is a compositing manager running; on all other platforms, it always returns true.
        connected (boolean):  <C> Return whether the user is connected or not to the Internet.
        ctime (boolean):  <C> Returns the current time in the format Wed Jan 02 02:03:55 1980\n\0
        currentDate (boolean):  <C> Returns the current date in the format yyyy/mm/dd, e.g. 2003/05/04.
        currentTime (boolean):  <C> Returns the current time in the format hh:mm:ss, e.g. 14:27:53.
        cutIdentifier (boolean):  <C> Returns the cut string.
        date (boolean):  <C> Returns the build date string.
        environmentFile (boolean):  <C> Returns the location of the application defaults file.
        evalVersion (boolean):  <C> This flag is now deprecated. Always returns false, as the eval version is no longer supported.
        file (boolean):  <C> Returns the file version string.
        fontInfo (boolean):  <C> Returns a string of the specifications of the fonts requested, and the specifications of the fonts that are actually being used.
        helpDataDirectory (boolean):  <C> Returns the help data directory.
        installedVersion (boolean):  <C> Returns the product version string.
        irix (boolean):  <C> Returns true if the operating system is Irix. Always false with support for Irix removed.
        is64 (boolean):  <C> Returns true if the application is 64 bit.
        languageResources (boolean):  <C> Returns a string array of the currently installed language resources. Each string entry consists of three elements delimited with a colon (':'). The first token is the locale code (ISO 639-1 language code followed by ISO 3166-1 country code).  The second token is the language name in English. This third token is the alpha-3 code (ISO 639-2).  For example English is represented as "en_US:English:enu".
        linux (boolean):  <C> Returns true if the operating system is Linux.
        linux64 (boolean):  <C> Returns true if the operating system is Linux 64 bit.
        liveUpdate (boolean):  <C> Returns Autodesk formatted product information.
        localizedResourceLocation (boolean):  <C> Returns the path to the top level of the localized resource directory, if we are running in an alternate language. Returns an empty string if we are running in the default language.
        ltVersion (boolean):  <C> Returns true if this is the Maya LT version of the application.
        macOS (boolean):  <C> Returns true if the operating system is Macintosh.
        macOSppc (boolean):  <C> Returns true if the operating system is a PowerPC Macintosh.
        macOSx86 (boolean):  <C> Returns true if the operating system is an Intel Macintosh.
        ntOS (boolean):  <C> Returns true if the operating system is Windows.
        operatingSystem (boolean):  <C> Returns the operating system type. Valid return types are "nt", "win64", "mac", "linux" and "linux64"
        operatingSystemVersion (boolean):  <C> Returns the operating system version. on Linux this returns the equivalent of uname -srvm
        preferences (boolean):  <C> Returns the location of the preferences directory.
        product (boolean):  <C> Returns the license product name.
        qtVersion (boolean):  <C> Returns Qt version string.
        tablet (boolean):  <C> Windows only.  Returns true if the PC is a Tablet PC.
        tabletMode (boolean):  <C> Windows 8 (and above) only.  If your device is a Tablet PC, then the convertible mode the device is currently running in.  Returns  either: tablet or laptop (keyboard attached). See the tablet flag.
        uiLanguage (boolean):  <C> Returns the language that Maya's running in.  Example return values include "en_US" for English and "ja_JP" for Japanese.
        uiLanguageForStartup (boolean):  <C> Returns the language that is used for Maya's next start up. This is read from config file and is rewritten after setting ui language in preference.
        uiLanguageIsLocalized (boolean):  <C> Returns true if we are running in an alternate language, not the default (English).
        uiLocaleLanguage (boolean):  <C> Returns the language locale of the OS. English is default.
        version (boolean):  <C> Returns the version string.
        win64 (boolean):  <C> Returns true if the operating system is Windows x64 based.
        windowManager (boolean):  <C> Returns the name of the Window Manager that is assumed to be running.
        windows (boolean):  <C> Returns true if the operating system is Windows based.
    Documentation:
        http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/about.html
    Examples:
        - import maya.cmds as cmds
        - 
        - cmds.about( )
        - 
        - version = cmds.about(v=True)
    """

def addAttr(query, q, edit, e, attributeType, binaryTag, cachedInternally, category,
            dataType, defaultValue, disconnectBehaviour, enumName, exists, fromPlugin,
            hasMaxValue, hasMinValue, hasSoftMaxValue, hasSoftMinValue, hidden,
            indexMatters, internalSet, keyable, longName, maxValue, minValue, multi,
            niceName, numberOfChildren, parent, proxy, readable, shortName, softMaxValue,
            softMinValue, storable, usedAsColor, usedAsFilename, usedAsProxy, writable):
    """
    addAttr is NOT undoable

    Args:
        query (boolean):   
        q (boolean):   
        edit (boolean):   
        e (boolean):   
        attributeType (string):  <C Q> Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        binaryTag (string):  <C Q> This flag is obsolete and does not do anything any more
        cachedInternally (boolean):  <C Q> Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached as this will make it impossible to set keyframes.
        category (string):  <C Q E M> An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however categories can not be removed once associated.
        dataType (string):  <C Q M> Specifies the data type.  See "setAttr" for more information on data type names.
        defaultValue (float):  <C Q E> Specifies the default value for the attribute (can only be used for numeric attributes).
        disconnectBehaviour (uint):  <C Q> defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        enumName (string):  <C Q E> Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        exists (boolean):  <C Q> Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        fromPlugin (boolean):  <C Q> Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        hasMaxValue (boolean):  <C Q E> Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        hasMinValue (boolean):  <C Q E> Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        hasSoftMaxValue (boolean):  <C Q> Flag indicating whether a numeric attribute has a soft maximum.
        hasSoftMinValue (boolean):  <C Q> Flag indicating whether a numeric attribute has a soft minimum.
        hidden (boolean):  <C Q> Will this attribute be hidden from the UI?
        indexMatters (boolean):  <C Q> Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        internalSet (boolean):  <C Q> Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        keyable (boolean):  <C Q> Is the attribute keyable by default?
        longName (string):  <C Q> Sets the long name of the attribute.
        maxValue (float):  <C Q E> Specifies the maximum value for the attribute (can only be used for numeric attributes).
        minValue (float):  <C Q E> Specifies the minimum value for the attribute (can only be used for numeric attributes).
        multi (boolean):  <C Q> Makes the new attribute a multi-attribute.
        niceName (string):  <C Q E> Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        numberOfChildren (uint):  <C Q> How many children will the new attribute have?
        parent (string):  <C Q> Attribute that is to be the new attribute's parent.
        proxy (string):  <C Q> Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        readable (boolean):  <C Q> Can outgoing connections be made from this attribute?
        shortName (string):  <C Q> Sets the short name of the attribute.
        softMaxValue (float):  <C Q E> Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        softMinValue (float):  <C Q E> Soft minimum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        storable (boolean):  <C Q> Can the attribute be stored out to a file?
        usedAsColor (boolean):  <C Q> Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt" as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        usedAsFilename (boolean):  <C Q> Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        usedAsProxy (boolean):  <C Q> Set if the specified attribute should be treated as a proxy to another attributes.
        writable (boolean):  <C Q> Can incoming connections be made to this attribute?
    Documentation:
        http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/addAttr.html
    Examples:
        - import maya.cmds as cmds
        - 
        - cmds.sphere( name='earth' )
        - # Add an attribute named ms/mass with a default value of 1 and a
        - # minimum value of 0.001 and a maximum of 10000.
        - #
        - cmds.addAttr( shortName='ms', longName='mass', defaultValue=1.0, minValue=0.001, maxValue=10000 )
        - 
        - # Add a multi attribute named ff/forcefield of type double3.
        - #
        - cmds.addAttr( shortName='ff', longName='forcefield', dataType='double3', multi=True )
        - 
        - # Add a compound attribute named sampson with children homeboy, midge,
        - # damien, elizabeth, and sweetpea of varying types
        - #
        - cmds.addAttr( longName='sampson', numberOfChildren=5, attributeType='compound' )
        - cmds.addAttr( longName='homeboy', attributeType='matrix', parent='sampson' )
        - cmds.addAttr( longName='midge', attributeType='message', parent='sampson' )
        - cmds.addAttr( longName='damien', attributeType='double', parent='sampson' )
        - cmds.addAttr( longName='elizabeth', attributeType='double', parent='sampson' )
        - cmds.addAttr( longName='sweetpea', attributeType='double', parent='sampson' )
        - 
        - # To add an attribute that is to be interpreted as a color the
        - # following attribute group must be used.
        - #
        - # Note that the word "float" must be in quotations since it is a
        - # MEL keyword.
        - #
        - cmds.addAttr( longName='rainbow', usedAsColor=True, attributeType='float3' )
        - cmds.addAttr( longName='redBow', attributeType='float', parent='rainbow' )
        - cmds.addAttr( longName='greenBow', attributeType='float', parent='rainbow' )
        - cmds.addAttr( longName='blueBow', attributeType='float', parent='rainbow' )
        - 
        - # Other legal attribute types that can be interpreted as colors need
        - # not specify the "-usedAsColor" flag as it will be assumed.  These
        - # include "-attributeType spectrum", "-attributeType reflectance",
        - # "-dataType spectrumRGB", and "-dataType reflectanceRGB".
        - #
        - cmds.addAttr( longName='implColor', dataType='spectrumRGB' )
        - cmds.addAttr( '.implColor', query=True, usedAsColor=True )
        - # Result: 1 #
        - 
        - # Add a double3 attribute named sanders with children bess, les and wes
        - #
        - cmds.addAttr( longName='sanders', attributeType='double3' )
        - cmds.addAttr( longName='bess', attributeType='double', parent='sanders' )
        - cmds.addAttr( longName='les', attributeType='double', parent='sanders' )
        - cmds.addAttr( longName='wes', attributeType='double', parent='sanders' )
        - 
        - # Create a ref Attribute
        - cmds.sphere( name='moon' )
        - cmds.select('earth');
        - cmds.addAttr(longName="someRefAttr", ref="moon.tx");
    """

def addDynamic():
    """
    addDynamic is NOT undoable

    Args:
        
    Documentation:
        http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/addDynamic.html
    Examples:
        - import maya.cmds as cmds
        - 
        - # Create an emitter
        - cmds.emitter( pos=(0, 0, 0), type='omni', r=100, sro=0, nuv=0, cye='none', cyi=1, spd=1, srn=0, nsp=1, tsp=0, mxd=0, mnd=0, dx=1, dy=0, dz=0, sp=0 )
        - # Result: emitter1 #
        - 
        - # Get the emitter to emit particles
        - cmds.particle()
        - # Result: particle2
        - cmds.connectDynamic( 'particle1', em='emitter1' )
        - 
        - # Create a particle to use as the source of the emitter
        - cmds.particle( p=((6.0, 0, 7.0), (6.0, 0, 2.0)), c=1 )
        - # Result: particle2
        - 
        - # Use particle2 as a source of the emitter
        - cmds.addDynamic( 'emitter1', 'particle2' )
    """

def addExtension(edit, e, nodeType, attributeType, binaryTag, cachedInternally, category,
                 dataType, defaultValue, disconnectBehaviour, enumName, exists, fromPlugin,
                 hasMaxValue, hasMinValue, hasSoftMaxValue, hasSoftMinValue, hidden,
                 indexMatters, internalSet, keyable, longName, maxValue, minValue, multi,
                 niceName, numberOfChildren, parent, proxy, readable, shortName, softMaxValue,
                 softMinValue, storable, usedAsColor, usedAsFilename, usedAsProxy, writable):
    """
    addExtension is undoable

    Args:
        edit (boolean):   
        e (boolean):   
        nodeType (string):  <C E> Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        attributeType (string):  <C Q> Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        binaryTag (string):  <C Q> This flag is obsolete and does not do anything any more
        cachedInternally (boolean):  <C Q> Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached as this will make it impossible to set keyframes.
        category (string):  <C Q E M> An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however categories can not be removed once associated.
        dataType (string):  <C Q M> Specifies the data type.  See "setAttr" for more information on data type names.
        defaultValue (float):  <C Q E> Specifies the default value for the attribute (can only be used for numeric attributes).
        disconnectBehaviour (uint):  <C Q> defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        enumName (string):  <C Q E> Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        exists (boolean):  <C Q> Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        fromPlugin (boolean):  <C Q> Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        hasMaxValue (boolean):  <C Q E> Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        hasMinValue (boolean):  <C Q E> Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        hasSoftMaxValue (boolean):  <C Q> Flag indicating whether a numeric attribute has a soft maximum.
        hasSoftMinValue (boolean):  <C Q> Flag indicating whether a numeric attribute has a soft minimum.
        hidden (boolean):  <C Q> Will this attribute be hidden from the UI?
        indexMatters (boolean):  <C Q> Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        internalSet (boolean):  <C Q> Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        keyable (boolean):  <C Q> Is the attribute keyable by default?
        longName (string):  <C Q> Sets the long name of the attribute.
        maxValue (float):  <C Q E> Specifies the maximum value for the attribute (can only be used for numeric attributes).
        minValue (float):  <C Q E> Specifies the minimum value for the attribute (can only be used for numeric attributes).
        multi (boolean):  <C Q> Makes the new attribute a multi-attribute.
        niceName (string):  <C Q E> Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        numberOfChildren (uint):  <C Q> How many children will the new attribute have?
        parent (string):  <C Q> Attribute that is to be the new attribute's parent.
        proxy (string):  <C Q> Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        readable (boolean):  <C Q> Can outgoing connections be made from this attribute?
        shortName (string):  <C Q> Sets the short name of the attribute.
        softMaxValue (float):  <C Q E> Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        softMinValue (float):  <C Q E> Soft minimum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        storable (boolean):  <C Q> Can the attribute be stored out to a file?
        usedAsColor (boolean):  <C Q> Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt" as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        usedAsFilename (boolean):  <C Q> Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        usedAsProxy (boolean):  <C Q> Set if the specified attribute should be treated as a proxy to another attributes.
        writable (boolean):  <C Q> Can incoming connections be made to this attribute?
    Documentation:
        http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/addExtension.html
    Examples:
        - import maya.cmds as cmds
        - 
        - # Add an attribute named ms/mass with a default value of 1 and a
        - # minimum value of 0.001 and a maximum of 10000 to all mesh shapes.
        - #
        - cmds.addExtension( nodeType='mesh', shortName='ms', longName='mass', defaultValue=1.0, minValue=0.001, maxValue=10000 )
        - 
        - # Add a multi attribute named ff/forcefield of type double3 to all mesh shapes.
        - #
        - cmds.addExtension( nodeType='mesh', shortName='ff', longName='forcefield', dataType='double3', multi=True )
        - 
        - # Add a compound attribute named sampson with children homeboy, midge,
        - # damien, elizabeth, and sweetpea of varying types to all choice nodes.
        - #
        - cmds.addExtension( nodeType='choice', longName='sampson', numberOfChildren=5, attributeType='compound' )
        - cmds.addExtension( nodeType='choice', longName='homeboy', attributeType='matrix', parent='sampson' )
        - cmds.addExtension( nodeType='choice', longName='midge', attributeType='message', parent='sampson' )
        - cmds.addExtension( nodeType='choice', longName='damien', attributeType='double', parent='sampson' )
        - cmds.addExtension( nodeType='choice', longName='elizabeth', attributeType='double', parent='sampson' )
        - cmds.addExtension( nodeType='choice', longName='sweetpea', attributeType='double', parent='sampson' )
        - 
        - # To add an attribute that is to be interpreted as a color the
        - # following attribute group must be used.
        - #
        - # Note that the word "float" must be in quotations since it is a
        - # MEL keyword.
        - #
        - cmds.addExtension( nodeType='phong', longName='rainbow', usedAsColor=True, attributeType='float3' )
        - cmds.addExtension( nodeType='phong', longName='redBow', attributeType='float', parent='rainbow' )
        - cmds.addExtension( nodeType='phong', longName='greenBow', attributeType='float', parent='rainbow' )
        - cmds.addExtension( nodeType='phong', longName='blueBow', attributeType='float', parent='rainbow' )
        - 
        - # Other legal attribute types that can be interpreted as colors need
        - # not specify the "-usedAsColor" flag as it will be assumed.  These
        - # include "-attributeType spectrum", "-attributeType reflectance",
        - # "-dataType spectrumRGB", and "-dataType reflectanceRGB".
        - #
        - cmds.addExtension( nodeType='phong', longName='implColor', dataType='spectrumRGB' )
        - 
        - # Add a double3 attribute named sanders with children bess, les and wes
        - # to all dag nodes, including shapes, transforms, and joints.
        - #
        - cmds.addExtension( nodeType='dagNode', longName='sanders', attributeType='double3' )
        - cmds.addExtension( nodeType='dagNode', longName='bess', attributeType='double', parent='sanders' )
        - cmds.addExtension( nodeType='dagNode', longName='les', attributeType='double', parent='sanders' )
        - cmds.addExtension( nodeType='dagNode', longName='wes', attributeType='double', parent='sanders' )
    """

def addMetadata(query, q, channelName, channelType, indexType, scene, streamName, structure):
    """
    addMetadata is NOT undoable

    Args:
        query (boolean):   
        q (boolean):   
        channelName (string):  <C Q> Name of the Channel type to which the structure is to be added (e.g. "vertex"). In query mode, this flag can accept a value.
        channelType (string):  <C Q> Obsolete - use the 'channelName' flag instead. In query mode, this flag can accept a value.
        indexType (string):  <C Q> Name of the index type the new Channel should be using. If not specified this defaults to a simple numeric index. Of the native types only a mesh "vertexFace" channel is different, using a "pair" index type. In query mode, this flag can accept a value.
        scene (boolean):  <C Q> Use this flag when you want to add metadata to the scene as a whole rather than to any individual nodes. If you use this flag and have nodes selected the nodes will be ignored and a warning will be displayed.
        streamName (string):  <C Q> Name of the empty stream being created. In query mode not specifying a value will return a list of streams on the named channel type. In query mode, this flag can accept a value.
        structure (string):  <C Q> Name of the structure which defines the metadata to be attached to the object. In query mode this will return the name of the structure attached at a given stream. In query mode, this flag can accept a value.
    Documentation:
        http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/addMetadata.html
    Examples:
        - import maya.cmds as cmds
        - 
        - import maya.cmds as cmds
        - cmds.polyPlane( name='p', ch=False )
        - cmds.select( 'pShape', replace=True )
        - cmds.dataStructure( format='raw', asString='name=IdStruct:int32=ID' )
        - cmds.dataStructure( format='raw', asString='name=OffStruct:float=Offset' )
        - cmds.dataStructure( format='raw', asString='name=OrgStruct:float[3]=Origin Point' )
        - # Add three metadata streams
        - cmds.addMetadata( streamName='IdStream', channelName='vertex', structure='IdStruct' )
        - cmds.addMetadata( streamName='OffStream', channelName='vertex', structure='OffStruct' )
        - cmds.addMetadata( streamName='OrgStream', channelName='edge', structure='OrgStruct' )
        - cmds.addMetadata( streamName='VFStream', channelName='vertexFace', indexType='pair', structure='OrgStruct' )
        - 
        - # Query for the list of all channel types possessing metadata
        - cmds.addMetadata( query=True, channelName=True )
        - # Return: ['edge', 'vertex', 'vertexFace'] #
        - 
        - # Query for the structure assigned to a specific stream
        - cmds.addMetadata( channelName='vertex', streamName='OffStream', query=True, structure=True )
        - # Return: 'OffStruct' #
        - 
        - # Query for the list of all streams on a specific channel type
        - cmds.addMetadata( channelName='vertex', query=True, streamName=True )
        - # Return: ['IdStream', 'OffStream'] #
        - 
        - # Query for the list of all streams
        - cmds.addMetadata( query=True, streamName=True )
        - # Return: ['IdStream', 'OffStream', 'OrgStream', 'VFStream'] #
        - 
        - # You can combine queries to answer more general questions about the
        - # metadata on an object. For example suppose you wanted to know the
        - # index type used by all Streams on the 'vertex' Channel.
        - # First extract the list of Streams on the Channel
        - streams = cmds.addMetadata( channelName='vertex', query=True, streamName=True )
        - # Loop through each Stream, querying the IndexType only for that Stream
        - for stream in streams:
        - 	indexType = cmds.addMetadata( channelName='vertex', streamName=stream, query=True, indexType=True )[0]
        - 	print 'Index type on %s is %s' % (stream, indexType)
    """

def addPP(attribute):
    """
    addPP is NOT undoable

    Args:
        attribute (string):  <C> Name of attribute to which you wish to add PP capability. Currently the only attribute supported is rate (for emitters).
    Documentation:
        http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/addPP.html
    Examples:
        - import maya.cmds as cmds
        - 
        - import maya.cmds as cmds
        - 
        - cmds.emitter( n='myEmitter1' )
        - cmds.particle( n='myParticle1' )
        - cmds.connectDynamic( 'myParticle1', em='myEmitter1' )
        - cmds.select( 'myParticle1' )
        - cmds.emitter( n='myEmitter2' )
        - cmds.particle( n='myParticle2' )
        - cmds.connectDynamic( 'myParticle2', em='myEmitter2' )
        - 
        - cmds.addPP( 'myEmitter2', atr='rate' )
        - 
        - # Suppose that myEmitter2 is owned by a particle shape, "myParticle1."
        - # addPP will add an attribute "myEmitter2RatePP" to myParticle1, will connect
        - # myParticle1.myEmitter2RatePP to myEmitter2.ratePP, and will set myEmitter2.useRatePP
        - # to true.
    """

def affectedNet(query, q, edit, e, type):
    """
    affectedNet is NOT undoable

    Args:
        query (boolean):   
        q (boolean):   
        edit (boolean):   
        e (boolean):   
        type (string):  <C> Get information from the given node type instead of one node
    Documentation:
        http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/affectedNet.html
    Examples:
        - import maya.cmds as cmds
        - 
        - # Create a network of this transform node's attributes that affect
        - # each other
        - cmds.affectedNet( 'transform1' )
        - 
        - # Create a network all of the transform shared attributes that affect
        - # each other
        - cmds.affectedNet( t='transform' )
        - 
        - # Create a network of the revolve and shape node type attributes that
        - # affect each other
        - cmds.affectedNet( t='revolve', t='shape' )
    """

