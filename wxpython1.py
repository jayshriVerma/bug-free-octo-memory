import wx

app = wx.App()

frame = wx.Frame(None, title='My application', style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
	| wx.SYSTEM_MENU | wx.CAPTION |	wx.CLOSE_BOX|wx.MINIMIZE_BOX ,size =(450,250),pos=(500,500))

frame.Show()
frame.Move(800, 250)


app.MainLoop()
'''wx.Frame(wx.Window parent, int id=-1, string title='', wx.Point pos=wx.DefaultPosition, 
    wx.Size size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, string name="frame")'''
    #size=(width,height)
