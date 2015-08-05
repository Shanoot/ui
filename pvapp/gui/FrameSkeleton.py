# -*- coding: utf-8 -*- ############################################################################# Python code generated with wxFormBuilder (version Sep 12 2010)## http://www.wxformbuilder.org/#### PLEASE DO "NOT" EDIT THIS FILE!###########################################################################import wx############################################################################# Class DataPanel###########################################################################class DataPanel ( wx.Panel ):		def __init__( self, parent ):		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )				bSizer1 = wx.BoxSizer( wx.HORIZONTAL )				self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )		self.m_scrolledWindow1.SetScrollRate( 5, 5 )		bSizer3 = wx.BoxSizer( wx.VERTICAL )				sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Waveform Parameters" ), wx.VERTICAL )				gSizer1 = wx.GridSizer( 0, 4, 0, 0 )				self.m_staticText1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Intensity (V)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText1.Wrap( -1 )		gSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Intensity = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer1.Add( self.m_Intensity, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText9 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"LED threshold\nCurrent (mA)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText9.Wrap( -1 )		gSizer1.Add( self.m_staticText9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )				self.m_Threshold = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"150", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer1.Add( self.m_Threshold, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText11 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Voltage Current\nConverter", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText11.Wrap( -1 )		gSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )				m_OutputChoices = [ u"High (2A/V)", u"Low (50mA/V)" ]		self.m_Output = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_OutputChoices, 0 )		self.m_Output.SetSelection( 0 )		gSizer1.Add( self.m_Output, 0, wx.ALL, 5 )				self.m_staticText10 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WaveFunction", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText10.Wrap( -1 )		gSizer1.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )				m_WaveformChoices = [ u"Cos", u"Sin", u"Square", u"Triangle", u"MattiasCustom", u"FrequencyScan" ]		self.m_Waveform = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_WaveformChoices, 0 )		self.m_Waveform.SetSelection( 0 )		gSizer1.Add( self.m_Waveform, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Illumination\nperiod (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText5.Wrap( -1 )		gSizer1.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Period = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer1.Add( self.m_Period, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText12 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Frequency (Hz)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText12.Wrap( -1 )		gSizer1.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_Frequency = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )		self.m_Frequency.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )				gSizer1.Add( self.m_Frequency, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText6 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Delay before\nillumination (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText6.Wrap( -1 )		gSizer1.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Offset_Before = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer1.Add( self.m_Offset_Before, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText7 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Delay after\nillumination (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText7.Wrap( -1 )		gSizer1.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Offset_After = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer1.Add( self.m_Offset_After, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				sbSizer2.Add( gSizer1, 0, wx.EXPAND, 5 )				bSizer3.Add( sbSizer2, 0, wx.EXPAND, 5 )				sbSizer_Processing = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Data transformations" ), wx.VERTICAL )				gSizer3 = wx.GridSizer( 0, 4, 0, 0 )				self.m_staticText8 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Samples to Average", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText8.Wrap( -1 )		gSizer3.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Averaging = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer3.Add( self.m_Averaging, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText3 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Bin Width", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText3.Wrap( -1 )		gSizer3.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Binning = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer3.Add( self.m_Binning, 0, wx.ALIGN_CENTER_VERTICAL, 5 )						gSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )				self.m_Name = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Number Of Data\nPoints: ", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_Name.Wrap( -1 )		gSizer3.Add( self.m_Name, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_DataPoint = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )		self.m_DataPoint.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )				gSizer3.Add( self.m_DataPoint, 0, wx.ALL, 5 )				sbSizer_Processing.Add( gSizer3, 1, wx.EXPAND, 5 )				bSizer3.Add( sbSizer_Processing, 0, wx.EXPAND, 5 )				bSizer4 = wx.BoxSizer( wx.HORIZONTAL )				self.m_Save = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )		bSizer4.Add( self.m_Save, 0, wx.ALL, 5 )				self.m_Load = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )		bSizer4.Add( self.m_Load, 0, wx.ALL, 5 )				self.m_LoadData = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Load Data", wx.DefaultPosition, wx.DefaultSize, 0 )		bSizer4.Add( self.m_LoadData, 0, wx.ALL, 5 )				bSizer3.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )				sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Invert Channels" ), wx.VERTICAL )				gSizer31 = wx.GridSizer( 0, 3, 0, 0 )				self.ChkBox_Ref = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Reference Intensity", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer31.Add( self.ChkBox_Ref, 0, wx.ALL, 5 )				self.ChkBox_PC = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"PC Signal", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer31.Add( self.ChkBox_PC, 0, wx.ALL, 5 )				self.ChkBox_PL = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"PL Signal", wx.DefaultPosition, wx.DefaultSize, 0 )		self.ChkBox_PL.SetValue(True) 		gSizer31.Add( self.ChkBox_PL, 0, wx.ALL, 5 )				sbSizer3.Add( gSizer31, 1, wx.EXPAND, 5 )				bSizer3.Add( sbSizer3, 0, wx.EXPAND, 5 )				gSizer8 = wx.GridSizer( 2, 2, 0, 0 )				self.GoButton = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.DefaultSize, 0 )		self.GoButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )		self.GoButton.SetBackgroundColour( wx.Colour( 98, 211, 22 ) )				gSizer8.Add( self.GoButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )				self.m_determineOffset = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Determine Offset", wx.DefaultPosition, wx.DefaultSize, 0 )		gSizer8.Add( self.m_determineOffset, 0, wx.ALL, 5 )				bSizer3.Add( gSizer8, 1, wx.EXPAND, 5 )				self.m_scrolledWindow1.SetSizer( bSizer3 )		self.m_scrolledWindow1.Layout()		bSizer3.Fit( self.m_scrolledWindow1 )		bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )				self.SetSizer( bSizer1 )		self.Layout()		bSizer1.Fit( self )				# Connect Events		self.m_scrolledWindow1.Bind( wx.EVT_CHAR, self.Run_Me )		self.m_Intensity.Bind( wx.EVT_CHAR, self.onChar )		self.m_Intensity.Bind( wx.EVT_TEXT, self.CurrentLimits )		self.m_Output.Bind( wx.EVT_CHOICE, self.CurrentLimits )		self.m_Period.Bind( wx.EVT_CHAR, self.onChar )		self.m_Period.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )		self.m_Offset_Before.Bind( wx.EVT_CHAR, self.onChar )		self.m_Offset_Before.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )		self.m_Offset_After.Bind( wx.EVT_CHAR, self.onChar )		self.m_Offset_After.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )		self.m_Averaging.Bind( wx.EVT_CHAR, self.onChar_int )		self.m_Binning.Bind( wx.EVT_CHAR, self.onChar_int )		self.m_Binning.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )		self.m_Save.Bind( wx.EVT_BUTTON, self.Save )		self.m_Load.Bind( wx.EVT_BUTTON, self.Load )		self.m_LoadData.Bind( wx.EVT_BUTTON, self.onLoadData )		self.ChkBox_Ref.Bind( wx.EVT_CHECKBOX, self.onInvert )		self.ChkBox_PC.Bind( wx.EVT_CHECKBOX, self.onInvert )		self.ChkBox_PL.Bind( wx.EVT_CHECKBOX, self.onInvert )		self.GoButton.Bind( wx.EVT_BUTTON, self.Perform_Standard_Measurement )		self.m_determineOffset.Bind( wx.EVT_BUTTON, self.onDetermineOffset )		def __del__( self ):		pass			# Virtual event handlers, overide them in your derived class	def Run_Me( self, event ):		event.Skip()		def onChar( self, event ):		event.Skip()		def CurrentLimits( self, event ):		event.Skip()				def Num_Data_Points_Update( self, event ):		event.Skip()						def onChar_int( self, event ):		event.Skip()				def Save( self, event ):		event.Skip()		def Load( self, event ):		event.Skip()		def onLoadData( self, event ):		event.Skip()		def onInvert( self, event ):		event.Skip()				def Perform_Standard_Measurement( self, event ):		event.Skip()		def onDetermineOffset( self, event ):		event.Skip()	