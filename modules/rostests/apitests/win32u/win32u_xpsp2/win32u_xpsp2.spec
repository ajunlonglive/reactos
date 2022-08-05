;
; ReactOS Operating System
;
; This file contains all win32k native api functions from win XP sp2
;

@ stdcall NtGdiAbortDoc(ptr)
@ stdcall NtGdiAbortPath(ptr)
@ stdcall NtGdiAddFontResourceW(wstr long long long long ptr)
@ stdcall NtGdiAddRemoteFontToDC(ptr ptr long ptr)
@ stdcall NtGdiAddFontMemResourceEx(ptr long ptr long ptr)
@ stdcall NtGdiRemoveMergeFont(ptr ptr)
@ stdcall NtGdiAddRemoteMMInstanceToDC(ptr ptr long)
@ stdcall NtGdiAlphaBlend(ptr long long long long ptr long long long long long ptr)
@ stdcall NtGdiAngleArc(ptr long long long long long)
@ stdcall NtGdiAnyLinkedFonts()
@ stdcall NtGdiFontIsLinked(ptr)
@ stdcall NtGdiArcInternal(long ptr long long long long long long long long)
@ stdcall NtGdiBeginPath(ptr)
@ stdcall NtGdiBitBlt(ptr long long long long ptr long long long long long)
@ stdcall NtGdiCancelDC(ptr)
@ stdcall NtGdiCheckBitmapBits(ptr ptr ptr long long long long ptr)
@ stdcall NtGdiCloseFigure(ptr)
@ stdcall NtGdiClearBitmapAttributes(ptr long)
@ stdcall NtGdiClearBrushAttributes(ptr long)
@ stdcall NtGdiColorCorrectPalette(ptr ptr long long ptr long)
@ stdcall NtGdiCombineRgn(ptr ptr ptr long)
@ stdcall NtGdiCombineTransform(ptr ptr ptr)
@ stdcall NtGdiComputeXformCoefficients(ptr)
@ stdcall NtGdiConsoleTextOut(ptr ptr long ptr)
@ stdcall NtGdiConvertMetafileRect(ptr ptr)
@ stdcall NtGdiCreateBitmap(long long long long ptr)
@ stdcall NtGdiCreateClientObj(long)
@ stdcall NtGdiCreateColorSpace(ptr)
@ stdcall NtGdiCreateColorTransform(ptr ptr ptr long ptr long ptr long)
@ stdcall NtGdiCreateCompatibleBitmap(ptr long long)
@ stdcall NtGdiCreateCompatibleDC(ptr)
@ stdcall NtGdiCreateDIBBrush(ptr long long long long ptr)
@ stdcall NtGdiCreateDIBitmapInternal(ptr long long long ptr ptr long long long long ptr)
@ stdcall NtGdiCreateDIBSection(ptr ptr long ptr long long long ptr ptr)
@ stdcall NtGdiCreateEllipticRgn(long long long long)
@ stdcall NtGdiCreateHalftonePalette(ptr)
@ stdcall NtGdiCreateHatchBrushInternal(long long long)
@ stdcall NtGdiCreateMetafileDC(ptr)
@ stdcall NtGdiCreatePaletteInternal(ptr long)
@ stdcall NtGdiCreatePatternBrushInternal(ptr long long)
@ stdcall NtGdiCreatePen(long long long ptr)
@ stdcall NtGdiCreateRectRgn(long long long long)
@ stdcall NtGdiCreateRoundRectRgn(long long long long long long)
@ stdcall NtGdiCreateServerMetaFile(long long ptr long long long)
@ stdcall NtGdiCreateSolidBrush(long ptr)
@ stdcall NtGdiD3dContextCreate(ptr ptr ptr ptr)
@ stdcall NtGdiD3dContextDestroy(ptr)
@ stdcall NtGdiD3dContextDestroyAll(ptr)
@ stdcall NtGdiD3dValidateTextureStageState(ptr)
@ stdcall NtGdiD3dDrawPrimitives2(ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiDdGetDriverState(ptr)
@ stdcall NtGdiDdAddAttachedSurface(ptr ptr ptr)
@ stdcall NtGdiDdAlphaBlt(ptr ptr ptr)
@ stdcall NtGdiDdAttachSurface(ptr ptr)
@ stdcall NtGdiDdBeginMoCompFrame(ptr ptr)
@ stdcall NtGdiDdBlt(ptr ptr ptr)
@ stdcall NtGdiDdCanCreateSurface(ptr ptr)
@ stdcall NtGdiDdCanCreateD3DBuffer(ptr ptr)
@ stdcall NtGdiDdColorControl(ptr ptr)
@ stdcall NtGdiDdCreateDirectDrawObject(ptr)
@ stdcall NtGdiDdCreateSurface(ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiDdCreateD3DBuffer(ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiDdCreateMoComp(ptr ptr)
@ stdcall NtGdiDdCreateSurfaceObject(ptr ptr ptr ptr ptr long)
@ stdcall NtGdiDdDeleteDirectDrawObject(ptr)
@ stdcall NtGdiDdDeleteSurfaceObject(ptr)
@ stdcall NtGdiDdDestroyMoComp(ptr ptr)
@ stdcall NtGdiDdDestroySurface(ptr long)
@ stdcall NtGdiDdDestroyD3DBuffer(ptr)
@ stdcall NtGdiDdEndMoCompFrame(ptr ptr)
@ stdcall NtGdiDdFlip(ptr ptr ptr ptr ptr)
@ stdcall NtGdiDdFlipToGDISurface(ptr ptr)
@ stdcall NtGdiDdGetAvailDriverMemory(ptr ptr)
@ stdcall NtGdiDdGetBltStatus(ptr ptr)
@ stdcall NtGdiDdGetDC(ptr ptr)
@ stdcall NtGdiDdGetDriverInfo(ptr ptr)
@ stdcall NtGdiDdGetDxHandle(ptr ptr long)
@ stdcall NtGdiDdGetFlipStatus(ptr ptr)
@ stdcall NtGdiDdGetInternalMoCompInfo(ptr ptr)
@ stdcall NtGdiDdGetMoCompBuffInfo(ptr ptr)
@ stdcall NtGdiDdGetMoCompGuids(ptr ptr)
@ stdcall NtGdiDdGetMoCompFormats(ptr ptr)
@ stdcall NtGdiDdGetScanLine(ptr ptr)
@ stdcall NtGdiDdLock(ptr ptr ptr)
@ stdcall NtGdiDdLockD3D(ptr ptr)
@ stdcall NtGdiDdQueryDirectDrawObject(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiDdQueryMoCompStatus(ptr ptr)
@ stdcall NtGdiDdReenableDirectDrawObject(ptr ptr)
@ stdcall NtGdiDdReleaseDC(ptr)
@ stdcall NtGdiDdRenderMoComp(ptr ptr)
@ stdcall NtGdiDdResetVisrgn(ptr ptr)
@ stdcall NtGdiDdSetColorKey(ptr ptr)
@ stdcall NtGdiDdSetExclusiveMode(ptr ptr)
@ stdcall NtGdiDdSetGammaRamp(ptr ptr ptr)
@ stdcall NtGdiDdCreateSurfaceEx(ptr ptr long)
@ stdcall NtGdiDdSetOverlayPosition(ptr ptr ptr)
@ stdcall NtGdiDdUnattachSurface(ptr ptr)
@ stdcall NtGdiDdUnlock(ptr ptr)
@ stdcall NtGdiDdUnlockD3D(ptr ptr)
@ stdcall NtGdiDdUpdateOverlay(ptr ptr ptr)
@ stdcall NtGdiDdWaitForVerticalBlank(ptr ptr)
@ stdcall NtGdiDvpCanCreateVideoPort(ptr ptr)
@ stdcall NtGdiDvpColorControl(ptr ptr)
@ stdcall NtGdiDvpCreateVideoPort(ptr ptr)
@ stdcall NtGdiDvpDestroyVideoPort(ptr ptr)
@ stdcall NtGdiDvpFlipVideoPort(ptr ptr ptr ptr)
@ stdcall NtGdiDvpGetVideoPortBandwidth(ptr ptr)
@ stdcall NtGdiDvpGetVideoPortField(ptr ptr)
@ stdcall NtGdiDvpGetVideoPortFlipStatus(ptr ptr)
@ stdcall NtGdiDvpGetVideoPortInputFormats(ptr ptr)
@ stdcall NtGdiDvpGetVideoPortLine(ptr ptr)
@ stdcall NtGdiDvpGetVideoPortOutputFormats(ptr ptr)
@ stdcall NtGdiDvpGetVideoPortConnectInfo(ptr ptr)
@ stdcall NtGdiDvpGetVideoSignalStatus(ptr ptr)
@ stdcall NtGdiDvpUpdateVideoPort(ptr ptr ptr ptr)
@ stdcall NtGdiDvpWaitForVideoPortSync(ptr ptr)
@ stdcall NtGdiDvpAcquireNotification(ptr ptr ptr)
@ stdcall NtGdiDvpReleaseNotification(ptr ptr)
@ stdcall NtGdiDxgGenericThunk(ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiDeleteClientObj(ptr)
@ stdcall NtGdiDeleteColorSpace(ptr)
@ stdcall NtGdiDeleteColorTransform(ptr ptr)
@ stdcall NtGdiDeleteObjectApp(ptr)
@ stdcall NtGdiDescribePixelFormat(ptr long long ptr)
@ stdcall NtGdiGetPerBandInfo(ptr ptr)
@ stdcall NtGdiDoBanding(ptr long ptr ptr)
@ stdcall NtGdiDoPalette(ptr long long ptr long long)
@ stdcall NtGdiDrawEscape(ptr long long ptr)
@ stdcall NtGdiEllipse(ptr long long long long)
@ stdcall NtGdiEnableEudc(long)
@ stdcall NtGdiEndDoc(ptr)
@ stdcall NtGdiEndPage(ptr)
@ stdcall NtGdiEndPath(ptr)
@ stdcall NtGdiEnumFontChunk(ptr ptr long ptr ptr)
@ stdcall NtGdiEnumFontClose(ptr)
@ stdcall NtGdiEnumFontOpen(ptr long long long wstr long ptr)
@ stdcall NtGdiEnumObjects(ptr long long ptr)
@ stdcall NtGdiEqualRgn(ptr ptr)
@ stdcall NtGdiEudcLoadUnloadLink(wstr long wstr long long long long)
@ stdcall NtGdiExcludeClipRect(ptr long long long long)
@ stdcall NtGdiExtCreatePen(long long long long ptr ptr long ptr long long ptr)
@ stdcall NtGdiExtCreateRegion(ptr long ptr)
@ stdcall NtGdiExtEscape(ptr ptr long long long ptr long ptr)
@ stdcall NtGdiExtFloodFill(ptr long long long long)
@ stdcall NtGdiExtGetObjectW(ptr long ptr)
@ stdcall NtGdiExtSelectClipRgn(ptr ptr long)
@ stdcall NtGdiExtTextOutW(ptr long long long ptr wstr long ptr long)
@ stdcall NtGdiFillPath(ptr)
@ stdcall NtGdiFillRgn(ptr ptr ptr)
@ stdcall NtGdiFlattenPath(ptr)
@ stdcall NtGdiFlushUserBatch()
@ stdcall NtGdiFlush()
@ stdcall NtGdiForceUFIMapping(ptr ptr)
@ stdcall NtGdiFrameRgn(ptr ptr ptr long long)
@ stdcall NtGdiFullscreenControl(long ptr long ptr ptr)
@ stdcall NtGdiGetAndSetDCDword(ptr long long ptr)
@ stdcall NtGdiGetAppClipBox(ptr ptr)
@ stdcall NtGdiGetBitmapBits(ptr long ptr)
@ stdcall NtGdiGetBitmapDimension(ptr ptr)
@ stdcall NtGdiGetBoundsRect(ptr ptr long)
@ stdcall NtGdiGetCharABCWidthsW(ptr long long ptr long ptr)
@ stdcall NtGdiGetCharacterPlacementW(ptr wstr long long ptr long)
@ stdcall NtGdiGetCharSet(ptr)
@ stdcall NtGdiGetCharWidthW(ptr long long ptr long ptr)
@ stdcall NtGdiGetCharWidthInfo(ptr ptr)
@ stdcall NtGdiGetColorAdjustment(ptr ptr)
@ stdcall NtGdiGetColorSpaceforBitmap(ptr)
@ stdcall NtGdiGetDCDword(ptr long ptr)
@ stdcall NtGdiGetDCforBitmap(ptr)
@ stdcall NtGdiGetDCObject(ptr long)
@ stdcall NtGdiGetDCPoint(ptr long ptr)
@ stdcall NtGdiGetDeviceCaps(ptr long)
@ stdcall NtGdiGetDeviceGammaRamp(ptr ptr)
@ stdcall NtGdiGetDeviceCapsAll(ptr ptr)
@ stdcall NtGdiGetDIBitsInternal(ptr ptr long long ptr ptr long long long)
@ stdcall NtGdiGetETM(ptr ptr)
@ stdcall NtGdiGetEudcTimeStampEx(wstr long long)
@ stdcall NtGdiGetFontData(ptr long long ptr long)
@ stdcall NtGdiGetFontResourceInfoInternalW(wstr long long long ptr ptr long)
@ stdcall NtGdiGetGlyphIndicesW(ptr wstr long ptr long)
@ stdcall NtGdiGetGlyphIndicesWInternal(ptr wstr long ptr long long)
@ stdcall NtGdiGetGlyphOutline(ptr long long ptr long ptr ptr long)
@ stdcall NtGdiGetKerningPairs(ptr long ptr)
@ stdcall NtGdiGetLinkedUFIs(ptr ptr long)
@ stdcall NtGdiGetMiterLimit(ptr ptr)
@ stdcall NtGdiGetMonitorID(ptr long ptr)
@ stdcall NtGdiGetNearestColor(ptr ptr)
@ stdcall NtGdiGetNearestPaletteIndex(ptr ptr)
@ stdcall NtGdiGetObjectBitmapHandle(ptr ptr)
@ stdcall NtGdiGetOutlineTextMetricsInternalW(ptr long ptr ptr)
@ stdcall NtGdiGetPath(ptr ptr ptr long)
@ stdcall NtGdiGetPixel(ptr long long)
@ stdcall NtGdiGetRandomRgn(ptr ptr long)
@ stdcall NtGdiGetRasterizerCaps(ptr long)
@ stdcall NtGdiGetRealizationInfo(ptr ptr ptr)
@ stdcall NtGdiGetRegionData(ptr long ptr)
@ stdcall NtGdiGetRgnBox(ptr ptr)
@ stdcall NtGdiGetServerMetaFileBits(ptr long ptr ptr ptr ptr ptr)
@ stdcall NtGdiGetSpoolMessage(long long long long)
@ stdcall NtGdiGetStats(ptr long long ptr long)
@ stdcall NtGdiGetStockObject(ptr)
@ stdcall NtGdiGetStringBitmapW(ptr wstr long ptr long)
@ stdcall NtGdiGetSystemPaletteUse(ptr)
@ stdcall NtGdiGetTextCharsetInfo(ptr ptr long)
@ stdcall NtGdiGetTextExtent(ptr wstr long ptr long)
@ stdcall NtGdiGetTextExtentExW(ptr wstr long long ptr ptr ptr long)
@ stdcall NtGdiGetTextFaceW(ptr long ptr long)
@ stdcall NtGdiGetTextMetricsW(ptr ptr long)
@ stdcall NtGdiGetTransform(ptr long ptr)
@ stdcall NtGdiGetUFI(ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiGetEmbUFI(ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiGetUFIPathname(ptr ptr wstr ptr long ptr ptr ptr ptr ptr)
@ stdcall NtGdiGetEmbedFonts()
@ stdcall NtGdiChangeGhostFont(ptr long)
@ stdcall NtGdiAddEmbFontToDC(ptr ptr)
@ stdcall NtGdiGetFontUnicodeRanges(ptr ptr)
@ stdcall NtGdiGetWidthTable(ptr long ptr long ptr ptr ptr)
@ stdcall NtGdiGradientFill(ptr ptr long ptr long long)
@ stdcall NtGdiHfontCreate(ptr long long long ptr)
@ stdcall NtGdiIcmBrushInfo(ptr ptr ptr ptr ptr ptr ptr long)
@ stdcall NtGdiInit()
@ stdcall NtGdiInitSpool()
@ stdcall NtGdiIntersectClipRect(ptr long long long long)
@ stdcall NtGdiInvertRgn(ptr ptr)
@ stdcall NtGdiLineTo(ptr long long)
@ stdcall NtGdiMakeFontDir(long ptr long wstr long)
@ stdcall NtGdiMakeInfoDC(ptr long)
@ stdcall NtGdiMaskBlt(ptr long long long long ptr long long ptr long long long long)
@ stdcall NtGdiModifyWorldTransform(ptr ptr long)
@ stdcall NtGdiMonoBitmap(ptr)
@ stdcall NtGdiMoveTo(ptr long long ptr)
@ stdcall NtGdiOffsetClipRgn(ptr long long)
@ stdcall NtGdiOffsetRgn(ptr long long)
@ stdcall NtGdiOpenDCW(ptr ptr ptr long long ptr ptr)
@ stdcall NtGdiPatBlt(ptr long long long long long)
@ stdcall NtGdiPolyPatBlt(ptr long ptr long long)
@ stdcall NtGdiPathToRegion(ptr)
@ stdcall NtGdiPlgBlt(ptr ptr ptr long long long long ptr long long long)
@ stdcall NtGdiPolyDraw(ptr ptr ptr long)
@ stdcall NtGdiPolyPolyDraw(ptr ptr ptr long long)
@ stdcall NtGdiPolyTextOutW(ptr ptr long long)
@ stdcall NtGdiPtInRegion(ptr long long)
@ stdcall NtGdiPtVisible(ptr long long)
@ stdcall NtGdiQueryFonts(ptr long ptr)
@ stdcall NtGdiQueryFontAssocInfo(ptr)
@ stdcall NtGdiRectangle(ptr long long long long)
@ stdcall NtGdiRectInRegion(ptr ptr)
@ stdcall NtGdiRectVisible(ptr ptr)
@ stdcall NtGdiRemoveFontResourceW(ptr long long long long ptr)
@ stdcall NtGdiRemoveFontMemResourceEx(ptr)
@ stdcall NtGdiResetDC(ptr ptr ptr ptr ptr)
@ stdcall NtGdiResizePalette(ptr long)
@ stdcall NtGdiRestoreDC(ptr long)
@ stdcall NtGdiRoundRect(ptr long long long long long long)
@ stdcall NtGdiSaveDC(ptr)
@ stdcall NtGdiScaleViewportExtEx(ptr long long long long ptr)
@ stdcall NtGdiScaleWindowExtEx(ptr long long long long ptr)
@ stdcall NtGdiSelectBitmap(ptr ptr)
@ stdcall NtGdiSelectBrush(ptr ptr)
@ stdcall NtGdiSelectClipPath(ptr long)
@ stdcall NtGdiSelectFont(ptr ptr)
@ stdcall NtGdiSelectPen(ptr ptr)
@ stdcall NtGdiSetBitmapAttributes(ptr long)
@ stdcall NtGdiSetBitmapBits(ptr long ptr)
@ stdcall NtGdiSetBitmapDimension(ptr long long ptr)
@ stdcall NtGdiSetBoundsRect(ptr ptr long)
@ stdcall NtGdiSetBrushAttributes(ptr long)
@ stdcall NtGdiSetBrushOrg(ptr long long ptr)
@ stdcall NtGdiSetColorAdjustment(ptr ptr)
@ stdcall NtGdiSetColorSpace(ptr ptr)
@ stdcall NtGdiSetDeviceGammaRamp(ptr ptr)
@ stdcall NtGdiSetDIBitsToDeviceInternal(ptr long long long long long long long long ptr ptr long long long long ptr)
@ stdcall NtGdiSetFontEnumeration(long)
@ stdcall NtGdiSetFontXform(ptr long long)
@ stdcall NtGdiSetIcmMode(ptr long long)
@ stdcall NtGdiSetLinkedUFIs(ptr ptr long)
@ stdcall NtGdiSetMagicColors(ptr long long)
@ stdcall NtGdiSetMetaRgn(ptr)
@ stdcall NtGdiSetMiterLimit(ptr long ptr)
@ stdcall NtGdiGetDeviceWidth(ptr)
@ stdcall NtGdiMirrorWindowOrg(ptr)
@ stdcall NtGdiSetLayout(ptr long long)
@ stdcall NtGdiSetPixel(ptr long long long)
@ stdcall NtGdiSetPixelFormat(ptr long)
@ stdcall NtGdiSetRectRgn(ptr long long long long)
@ stdcall NtGdiSetSystemPaletteUse(ptr long)
@ stdcall NtGdiSetTextJustification(ptr long long)
@ stdcall NtGdiSetupPublicCFONT(ptr ptr long)
@ stdcall NtGdiSetVirtualResolution(ptr long long long long)
@ stdcall NtGdiSetSizeDevice(ptr long long)
@ stdcall NtGdiStartDoc(ptr ptr ptr long)
@ stdcall NtGdiStartPage(ptr)
@ stdcall NtGdiStretchBlt(ptr long long long long ptr long long long long long long)
@ stdcall NtGdiStretchDIBitsInternal(ptr long long long long long long long long ptr ptr long long long long ptr)
@ stdcall NtGdiStrokeAndFillPath(ptr)
@ stdcall NtGdiStrokePath(ptr)
@ stdcall NtGdiSwapBuffers(ptr)
@ stdcall NtGdiTransformPoints(ptr ptr ptr long long)
@ stdcall NtGdiTransparentBlt(ptr long long long long  ptr long long long long long)
@ stdcall NtGdiUnloadPrinterDriver(wstr long)
@ stdcall NtGdiUnmapMemFont(ptr)
@ stdcall NtGdiUnrealizeObject(ptr)
@ stdcall NtGdiUpdateColors(ptr)
@ stdcall NtGdiWidenPath(ptr)
@ stdcall NtUserActivateKeyboardLayout(ptr long)
@ stdcall NtUserAlterWindowStyle(long long long)
@ stdcall NtUserAssociateInputContext(long long long)
@ stdcall NtUserAttachThreadInput(long long long)
@ stdcall NtUserBeginPaint(ptr ptr)
@ stdcall NtUserBitBltSysBmp(ptr long long long long long long long)
@ stdcall NtUserBlockInput(long)
@ stdcall NtUserBuildHimcList(long long long long)
@ stdcall NtUserBuildHwndList(ptr ptr long long long ptr ptr)
@ stdcall NtUserBuildNameList(ptr long ptr ptr)
@ stdcall NtUserBuildPropList(ptr ptr long ptr)
@ stdcall NtUserCallHwnd(ptr long)
@ stdcall NtUserCallHwndLock(ptr long)
@ stdcall NtUserCallHwndOpt(ptr long)
@ stdcall NtUserCallHwndParam(ptr long long)
@ stdcall NtUserCallHwndParamLock(ptr long long)
@ stdcall NtUserCallMsgFilter(ptr long)
@ stdcall NtUserCallNextHookEx(long ptr ptr long)
@ stdcall NtUserCallNoParam(long)
@ stdcall NtUserCallOneParam(ptr long)
@ stdcall NtUserCallTwoParam(ptr ptr long)
@ stdcall NtUserChangeClipboardChain(ptr ptr)
@ stdcall NtUserChangeDisplaySettings(ptr ptr ptr long ptr)
@ stdcall NtUserCheckImeHotKey(long long)
@ stdcall NtUserCheckMenuItem(ptr long long)
@ stdcall NtUserChildWindowFromPointEx(ptr long long long)
@ stdcall NtUserClipCursor(ptr)
@ stdcall NtUserCloseClipboard()
@ stdcall NtUserCloseDesktop(ptr)
@ stdcall NtUserCloseWindowStation(ptr)
@ stdcall NtUserConsoleControl(long long long)
@ stdcall NtUserConvertMemHandle(ptr long)
@ stdcall NtUserCopyAcceleratorTable(ptr ptr long)
@ stdcall NtUserCountClipboardFormats()
@ stdcall NtUserCreateAcceleratorTable(ptr ptr)
@ stdcall NtUserCreateCaret(ptr ptr long long)
@ stdcall NtUserCreateDesktop(ptr ptr ptr long long)
@ stdcall NtUserCreateInputContext(long)
@ stdcall NtUserCreateLocalMemHandle(ptr ptr long ptr)
@ stdcall NtUserCreateWindowEx(long ptr ptr ptr long long long long long ptr ptr ptr ptr long ptr)
@ stdcall NtUserCreateWindowStation(ptr long long long long long long)
@ stdcall NtUserDdeGetQualityOfService(ptr ptr ptr)
@ stdcall NtUserDdeInitialize(long long long long long)
@ stdcall NtUserDdeSetQualityOfService(ptr ptr ptr)
@ stdcall NtUserDeferWindowPos(ptr ptr ptr long long long long long)
@ stdcall NtUserDefSetText(ptr ptr)
@ stdcall NtUserDeleteMenu(ptr long long)
@ stdcall NtUserDestroyAcceleratorTable(ptr)
@ stdcall NtUserDestroyCursor(ptr long)
@ stdcall NtUserDestroyInputContext(long)
@ stdcall NtUserDestroyMenu(ptr)
@ stdcall NtUserDestroyWindow(ptr)
@ stdcall NtUserDisableThreadIme(long)
@ stdcall NtUserDispatchMessage(ptr)
@ stdcall NtUserDragDetect(ptr ptr long)
@ stdcall NtUserDragObject(ptr ptr long long ptr)
@ stdcall NtUserDrawAnimatedRects(ptr long ptr ptr)
@ stdcall NtUserDrawCaption(ptr ptr ptr long)
@ stdcall NtUserDrawCaptionTemp(ptr ptr ptr ptr ptr ptr long)
@ stdcall NtUserDrawIconEx(ptr long long ptr long long long ptr long long ptr)
@ stdcall NtUserDrawMenuBarTemp(ptr ptr ptr ptr ptr)
@ stdcall NtUserEmptyClipboard()
@ stdcall NtUserEnableMenuItem(ptr long long)
@ stdcall NtUserEnableScrollBar(ptr long long)
@ stdcall NtUserEndDeferWindowPosEx(ptr long)
@ stdcall NtUserEndMenu()
@ stdcall NtUserEndPaint(ptr ptr)
@ stdcall NtUserEnumDisplayDevices(ptr long ptr long)
@ stdcall NtUserEnumDisplayMonitors(ptr ptr ptr ptr)
@ stdcall NtUserEnumDisplaySettings(ptr long ptr long)
@ stdcall NtUserEvent(long)
@ stdcall NtUserExcludeUpdateRgn(ptr ptr)
@ stdcall NtUserFillWindow(ptr ptr ptr ptr)
@ stdcall NtUserFindExistingCursorIcon(ptr ptr ptr)
@ stdcall NtUserFindWindowEx(ptr ptr ptr ptr long)
@ stdcall NtUserFlashWindowEx(ptr)
@ stdcall NtUserGetAltTabInfo(ptr long ptr wstr long long)
@ stdcall NtUserGetAncestor(ptr long)
@ stdcall NtUserGetAppImeLevel(long)
@ stdcall NtUserGetAsyncKeyState(long)
@ stdcall NtUserGetAtomName(long ptr)
@ stdcall NtUserGetCaretBlinkTime()
@ stdcall NtUserGetCaretPos(ptr)
@ stdcall NtUserGetClassInfo(ptr ptr ptr ptr long)
@ stdcall NtUserGetClassName(ptr long ptr)
@ stdcall NtUserGetClipboardData(long ptr)
@ stdcall NtUserGetClipboardFormatName(long wstr ptr)
@ stdcall NtUserGetClipboardOwner()
@ stdcall NtUserGetClipboardSequenceNumber()
@ stdcall NtUserGetClipboardViewer()
@ stdcall NtUserGetClipCursor(ptr)
@ stdcall NtUserGetComboBoxInfo(ptr ptr)
@ stdcall NtUserGetControlBrush(ptr ptr long)
@ stdcall NtUserGetControlColor(ptr ptr ptr long)
@ stdcall NtUserGetCPD(ptr long ptr)
@ stdcall NtUserGetCursorFrameInfo(ptr long ptr ptr)
@ stdcall NtUserGetCursorInfo(ptr)
@ stdcall NtUserGetDC(ptr)
@ stdcall NtUserGetDCEx(ptr ptr long)
@ stdcall NtUserGetDoubleClickTime()
@ stdcall NtUserGetForegroundWindow()
@ stdcall NtUserGetGuiResources(ptr long)
@ stdcall NtUserGetGUIThreadInfo(long ptr)
@ stdcall NtUserGetIconInfo(ptr ptr ptr ptr ptr long)
@ stdcall NtUserGetIconSize(ptr long ptr ptr)
@ stdcall NtUserGetImeHotKey(long long long long)
@ stdcall NtUserGetImeInfoEx(long long)
@ stdcall NtUserGetInternalWindowPos(ptr ptr ptr)
@ stdcall NtUserGetKeyboardLayoutList(long ptr)
@ stdcall NtUserGetKeyboardLayoutName(ptr)
@ stdcall NtUserGetKeyboardState(ptr)
@ stdcall NtUserGetKeyNameText(long wstr long)
@ stdcall NtUserGetKeyState(long)
@ stdcall NtUserGetListBoxInfo(ptr)
@ stdcall NtUserGetMenuBarInfo(ptr long long ptr)
@ stdcall NtUserGetMenuIndex(ptr ptr)
@ stdcall NtUserGetMenuItemRect(ptr ptr long ptr)
@ stdcall NtUserGetMessage(ptr ptr long long)
@ stdcall NtUserGetMouseMovePointsEx(long ptr ptr long long)
@ stdcall NtUserGetObjectInformation(ptr long ptr long ptr)
@ stdcall NtUserGetOpenClipboardWindow()
@ stdcall NtUserGetPriorityClipboardFormat(ptr long)
@ stdcall NtUserGetProcessWindowStation()
@ stdcall NtUserGetRawInputBuffer(ptr ptr long)
@ stdcall NtUserGetRawInputData(ptr long ptr ptr long)
@ stdcall NtUserGetRawInputDeviceInfo(ptr long ptr ptr)
@ stdcall NtUserGetRawInputDeviceList(ptr ptr long)
@ stdcall NtUserGetRegisteredRawInputDevices(ptr ptr long)
@ stdcall NtUserGetScrollBarInfo(ptr long ptr)
@ stdcall NtUserGetSystemMenu(ptr long)
@ stdcall NtUserGetThreadDesktop(long long)
@ stdcall NtUserGetThreadState(ptr)
@ stdcall NtUserGetTitleBarInfo(ptr ptr)
@ stdcall NtUserGetUpdateRect(ptr ptr long)
@ stdcall NtUserGetUpdateRgn(ptr ptr long)
@ stdcall NtUserGetWindowDC(ptr)
@ stdcall NtUserGetWindowPlacement(ptr ptr)
@ stdcall NtUserGetWOWClass(ptr ptr)
@ stdcall NtUserHardErrorControl(long long long)
@ stdcall NtUserHideCaret(ptr)
@ stdcall NtUserHiliteMenuItem(ptr ptr long long)
@ stdcall NtUserImpersonateDdeClientWindow(ptr ptr)
@ stdcall NtUserInitialize(long ptr ptr)
@ stdcall NtUserInitializeClientPfnArrays(ptr ptr ptr ptr)
@ stdcall NtUserInitTask(long long long long long long long long long long long long)
@ stdcall NtUserInternalGetWindowText(ptr wstr ptr)
@ stdcall NtUserInvalidateRect(ptr ptr long)
@ stdcall NtUserInvalidateRgn(ptr ptr long)
@ stdcall NtUserIsClipboardFormatAvailable(long)
@ stdcall NtUserKillTimer(ptr ptr)
@ stdcall NtUserLoadKeyboardLayoutEx(ptr long ptr ptr ptr long long)
@ stdcall NtUserLockWindowStation(ptr)
@ stdcall NtUserLockWindowUpdate(ptr)
@ stdcall NtUserLockWorkStation()
@ stdcall NtUserMapVirtualKeyEx(long long long ptr)
@ stdcall NtUserMenuItemFromPoint(ptr ptr long long)
@ stdcall NtUserMessageCall(ptr long ptr ptr ptr long long)
@ stdcall NtUserMinMaximize(ptr long long)
@ stdcall NtUserMNDragLeave()
@ stdcall NtUserMNDragOver(long long)
@ stdcall NtUserModifyUserStartupInfoFlags(long long)
@ stdcall NtUserMoveWindow(ptr long long long long long)
@ stdcall NtUserNotifyIMEStatus(long long long)
@ stdcall NtUserNotifyProcessCreate(long long long long)
@ stdcall NtUserNotifyWinEvent(long long long long)
@ stdcall NtUserOpenClipboard(ptr long)
@ stdcall NtUserOpenDesktop(ptr long long)
@ stdcall NtUserOpenInputDesktop(long long long)
@ stdcall NtUserOpenWindowStation(ptr long)
@ stdcall NtUserPaintDesktop(ptr)
@ stdcall NtUserPeekMessage(ptr ptr long long long)
@ stdcall NtUserPostMessage(ptr long long long)
@ stdcall NtUserPostThreadMessage(long long long long)
@ stdcall NtUserPrintWindow(ptr ptr long)
@ stdcall NtUserProcessConnect(ptr ptr long)
@ stdcall NtUserQueryInformationThread(long long long long long)
@ stdcall NtUserQueryInputContext(long long)
@ stdcall NtUserQuerySendMessage(long)
@ stdcall NtUserQueryUserCounters(long long long long long)
@ stdcall NtUserQueryWindow(ptr long)
@ stdcall NtUserRealChildWindowFromPoint(ptr long long)
@ stdcall NtUserRealInternalGetMessage(ptr ptr long long long long)
@ stdcall NtUserRealWaitMessageEx(long long)
@ stdcall NtUserRedrawWindow(ptr ptr ptr long)
@ stdcall NtUserRegisterClassExWOW(ptr ptr ptr ptr long long ptr)
@ stdcall NtUserRegisterUserApiHook(ptr ptr)
@ stdcall NtUserRegisterHotKey(ptr long long long)
@ stdcall NtUserRegisterRawInputDevices(ptr long long)
@ stdcall NtUserRegisterTasklist(long)
@ stdcall NtUserRegisterWindowMessage(ptr)
@ stdcall NtUserRemoveMenu(ptr long long)
@ stdcall NtUserRemoveProp(ptr long)
@ stdcall NtUserResolveDesktop(long long long long)
@ stdcall NtUserResolveDesktopForWOW(long)
@ stdcall NtUserSBGetParms(ptr long ptr ptr)
@ stdcall NtUserScrollDC(ptr long long ptr ptr ptr ptr)
@ stdcall NtUserScrollWindowEx(ptr long long ptr ptr ptr ptr long)
@ stdcall NtUserSelectPalette(ptr ptr long)
@ stdcall NtUserSendInput(long ptr long)
@ stdcall NtUserSetActiveWindow(ptr)
@ stdcall NtUserSetAppImeLevel(long long)
@ stdcall NtUserSetCapture(ptr)
@ stdcall NtUserSetClassLong(ptr long ptr long)
@ stdcall NtUserSetClassWord(ptr long long)
@ stdcall NtUserSetClipboardData(long ptr ptr)
@ stdcall NtUserSetClipboardViewer(ptr)
@ stdcall NtUserSetConsoleReserveKeys(long long)
@ stdcall NtUserSetCursor(ptr)
@ stdcall NtUserSetCursorContents(ptr ptr)
@ stdcall NtUserSetCursorIconData(ptr ptr ptr ptr)
@ stdcall NtUserSetDbgTag(long long)
@ stdcall NtUserSetFocus(ptr)
@ stdcall NtUserSetImeHotKey(long long long long long)
@ stdcall NtUserSetImeInfoEx(long)
@ stdcall NtUserSetImeOwnerWindow(long long)
@ stdcall NtUserSetInformationProcess(long long long long)
@ stdcall NtUserSetInformationThread(ptr long ptr long)
@ stdcall NtUserSetInternalWindowPos(ptr long ptr ptr)
@ stdcall NtUserSetKeyboardState(ptr)
@ stdcall NtUserSetLogonNotifyWindow(ptr)
@ stdcall NtUserSetMenu(ptr ptr long)
@ stdcall NtUserSetMenuContextHelpId(ptr long)
@ stdcall NtUserSetMenuDefaultItem(ptr long long)
@ stdcall NtUserSetMenuFlagRtoL(ptr)
@ stdcall NtUserSetObjectInformation(ptr long ptr long)
@ stdcall NtUserSetParent(ptr ptr)
@ stdcall NtUserSetProcessWindowStation(ptr)
@ stdcall NtUserSetProp(ptr long ptr)
@ stdcall NtUserSetRipFlags(long long)
@ stdcall NtUserSetScrollInfo(ptr long ptr long)
@ stdcall NtUserSetShellWindowEx(ptr ptr)
@ stdcall NtUserSetSysColors(long ptr ptr long)
@ stdcall NtUserSetSystemCursor(ptr long)
@ stdcall NtUserSetSystemMenu(ptr ptr)
@ stdcall NtUserSetSystemTimer(ptr ptr long ptr)
@ stdcall NtUserSetThreadDesktop(ptr)
@ stdcall NtUserSetThreadLayoutHandles(long long)
@ stdcall NtUserSetThreadState(long long)
@ stdcall NtUserSetTimer(ptr ptr long ptr)
@ stdcall NtUserSetWindowFNID(ptr long)
@ stdcall NtUserSetWindowLong(ptr long long long)
@ stdcall NtUserSetWindowPlacement(ptr ptr)
@ stdcall NtUserSetWindowPos(ptr ptr long long long long long)
@ stdcall NtUserSetWindowRgn(ptr ptr long)
@ stdcall NtUserSetWindowsHookAW(long ptr long)
@ stdcall NtUserSetWindowsHookEx(ptr ptr long long ptr long)
@ stdcall NtUserSetWindowStationUser(long long long long)
@ stdcall NtUserSetWindowWord(ptr long long)
@ stdcall NtUserSetWinEventHook(long long ptr ptr ptr long long long)
@ stdcall NtUserShowCaret(ptr)
@ stdcall NtUserShowScrollBar(ptr long long)
@ stdcall NtUserShowWindow(ptr long)
@ stdcall NtUserShowWindowAsync(ptr long)
@ stdcall NtUserSoundSentry()
@ stdcall NtUserSwitchDesktop(ptr)
@ stdcall NtUserSystemParametersInfo(long long ptr long)
@ stdcall NtUserTestForInteractiveUser(long)
@ stdcall NtUserThunkedMenuInfo(ptr ptr)
@ stdcall NtUserThunkedMenuItemInfo(ptr long long long ptr ptr)
@ stdcall NtUserToUnicodeEx(long long ptr wstr long long ptr)
@ stdcall NtUserTrackMouseEvent(ptr)
@ stdcall NtUserTrackPopupMenuEx(ptr long long long ptr ptr)
@ stdcall NtUserCalcMenuBar(long long long long long)
@ stdcall NtUserPaintMenuBar(long long long long long long)
@ stdcall NtUserTranslateAccelerator(ptr ptr ptr)
@ stdcall NtUserTranslateMessage(ptr long)
@ stdcall NtUserUnhookWindowsHookEx(ptr)
@ stdcall NtUserUnhookWinEvent(ptr)
@ stdcall NtUserUnloadKeyboardLayout(ptr)
@ stdcall NtUserUnlockWindowStation(ptr)
@ stdcall NtUserUnregisterClass(ptr ptr ptr)
@ stdcall NtUserUnregisterUserApiHook()
@ stdcall NtUserUnregisterHotKey(ptr long)
@ stdcall NtUserUpdateInputContext(long long long)
@ stdcall NtUserUpdateInstance(long long long)
@ stdcall NtUserUpdateLayeredWindow(ptr ptr ptr ptr ptr ptr long long ptr)
@ stdcall NtUserGetLayeredWindowAttributes(ptr ptr ptr ptr)
@ stdcall NtUserSetLayeredWindowAttributes(ptr long long long)
@ stdcall NtUserUpdatePerUserSystemParameters(long long)
@ stdcall NtUserUserHandleGrantAccess(ptr ptr long)
@ stdcall NtUserValidateHandleSecure(ptr long)
@ stdcall NtUserValidateRect(ptr ptr)
@ stdcall NtUserValidateTimerCallback(ptr ptr ptr)
@ stdcall NtUserVkKeyScanEx(long ptr long)
@ stdcall NtUserWaitForInputIdle(ptr long long)
@ stdcall NtUserWaitForMsgAndEvent(long)
@ stdcall NtUserWaitMessage()
@ stdcall NtUserWin32PoolAllocationStats(long long long long long long)
@ stdcall NtUserWindowFromPoint(long long)
@ stdcall NtUserYieldTask()
@ stdcall NtUserRemoteConnect(long long long)
@ stdcall NtUserRemoteRedrawRectangle(long long long long)
@ stdcall NtUserRemoteRedrawScreen()
@ stdcall NtUserRemoteStopScreenUpdates()
@ stdcall NtUserCtxDisplayIOCtl(long long long)
@ stdcall NtGdiEngAssociateSurface(ptr ptr long)
@ stdcall NtGdiEngCreateBitmap(long long long long long ptr)
@ stdcall NtGdiEngCreateDeviceSurface(ptr long long long)
@ stdcall NtGdiEngCreateDeviceBitmap(ptr long long long)
@ stdcall NtGdiEngCreatePalette(long long ptr long long long)
@ stdcall NtGdiEngComputeGlyphSet(ptr ptr ptr)
@ stdcall NtGdiEngCopyBits(ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiEngDeletePalette(ptr)
@ stdcall NtGdiEngDeleteSurface(ptr)
@ stdcall NtGdiEngEraseSurface(ptr ptr long)
@ stdcall NtGdiEngUnlockSurface(ptr)
@ stdcall NtGdiEngLockSurface(ptr)
@ stdcall NtGdiEngBitBlt(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiEngStretchBlt(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr long)
@ stdcall NtGdiEngPlgBlt(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr long)
@ stdcall NtGdiEngMarkBandingSurface(ptr)
@ stdcall NtGdiEngStrokePath(ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiEngFillPath(ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiEngStrokeAndFillPath(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiEngPaint(ptr ptr ptr ptr ptr)
@ stdcall NtGdiEngLineTo(ptr ptr ptr long long long long ptr ptr)
@ stdcall NtGdiEngAlphaBlend(ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiEngGradientFill(ptr ptr ptr ptr long ptr long ptr ptr long)
@ stdcall NtGdiEngTransparentBlt(ptr ptr ptr ptr ptr ptr long long)
@ stdcall NtGdiEngTextOut(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall NtGdiEngStretchBltROP(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr long ptr long)
@ stdcall NtGdiXLATEOBJ_cGetPalette(ptr long long ptr)
@ stdcall NtGdiXLATEOBJ_iXlate(ptr long)
@ stdcall NtGdiXLATEOBJ_hGetColorTransform(ptr)
@ stdcall NtGdiCLIPOBJ_bEnum(ptr long long)
@ stdcall NtGdiCLIPOBJ_cEnumStart(ptr long long long long)
@ stdcall NtGdiCLIPOBJ_ppoGetPath(ptr)
@ stdcall NtGdiEngDeletePath(ptr)
@ stdcall NtGdiEngCreateClip()
@ stdcall NtGdiEngDeleteClip(ptr)
@ stdcall NtGdiBRUSHOBJ_ulGetBrushColor(ptr)
@ stdcall NtGdiBRUSHOBJ_pvAllocRbrush(ptr long)
@ stdcall NtGdiBRUSHOBJ_pvGetRbrush(ptr)
@ stdcall NtGdiBRUSHOBJ_hGetColorTransform(ptr)
@ stdcall NtGdiXFORMOBJ_bApplyXform(ptr ptr long long ptr)
@ stdcall NtGdiXFORMOBJ_iGetXform(ptr ptr)
@ stdcall NtGdiFONTOBJ_vGetInfo(ptr long ptr)
@ stdcall NtGdiFONTOBJ_pxoGetXform(ptr)
@ stdcall NtGdiFONTOBJ_cGetGlyphs(ptr long long ptr ptr)
@ stdcall NtGdiFONTOBJ_pifi(ptr)
@ stdcall NtGdiFONTOBJ_pfdg(ptr)
@ stdcall NtGdiFONTOBJ_pQueryGlyphAttrs(ptr long)
@ stdcall NtGdiFONTOBJ_pvTrueTypeFontFile(ptr ptr)
@ stdcall NtGdiFONTOBJ_cGetAllGlyphHandles(ptr ptr)
@ stdcall NtGdiSTROBJ_bEnum(ptr ptr ptr)
@ stdcall NtGdiSTROBJ_bEnumPositionsOnly(ptr ptr ptr)
@ stdcall NtGdiSTROBJ_bGetAdvanceWidths(ptr long long ptr)
@ stdcall NtGdiSTROBJ_vEnumStart(ptr)
@ stdcall NtGdiSTROBJ_dwGetCodePage(ptr)
@ stdcall NtGdiPATHOBJ_vGetBounds(ptr ptr)
@ stdcall NtGdiPATHOBJ_bEnum(ptr ptr)
@ stdcall NtGdiPATHOBJ_vEnumStart(ptr)
@ stdcall NtGdiPATHOBJ_vEnumStartClipLines(ptr ptr ptr ptr)
@ stdcall NtGdiPATHOBJ_bEnumClipLines(ptr long ptr)
@ stdcall NtGdiGetDhpdev(ptr)
@ stdcall NtGdiEngCheckAbort(ptr)
@ stdcall NtGdiHT_Get8BPPFormatPalette(ptr long long long)
@ stdcall NtGdiHT_Get8BPPMaskPalette(ptr long long long long long)
@ stdcall NtGdiUpdateTransform(ptr)
@ stdcall NtGdiSetPUMPDOBJ(ptr long ptr ptr)
@ stdcall NtGdiBRUSHOBJ_DeleteRbrush(ptr ptr)
@ stdcall NtGdiUMPDEngFreeUserMem(ptr)
@ stdcall NtGdiDrawStream(ptr long ptr)
