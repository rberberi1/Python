def cam():
    import tkinter
    from tkinter import messagebox
    import cv2
    import PIL.Image, PIL.ImageTk
    import time

    class App:
        def __init__(self, window, window_title, video_source=0): 
            self.window = window
            self.window.title(window_title)
            self.video_source = video_source

            self.vid = MyVideoCapture(self.video_source)
            self.canvas = tkinter.Canvas(window, height=self.vid.height, width=self.vid.width)
            self.canvas.pack()

            btn_frame = tkinter.Frame(window, background='Black')
            btn_frame.place(x=0, y=0)

            self.btn_snapshot = tkinter.Button(btn_frame, text='Snapshot', command=self.snapshot, width=20, bg='black', fg='white')
            self.btn_snapshot.pack(side="left", padx=10, pady=10)

            self.delay = 15
            self.update()

            self.window.mainloop()

        def snapshot(self):
            ret, frame = self.vid.get_frame()
            if ret:
                cv2.imwrite('My Capture ' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                messagebox.showinfo('Notification', 'Image Saved')

        def update(self):
            ret, frame = self.vid.get_frame()

            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

            self.window.after(self.delay, self.update)

    class MyVideoCapture:
        def __init__(self, video_source=0):
            self.vid = cv2.VideoCapture(video_source)
            if not self.vid.isOpened():
                raise ValueError('Unable to open video source', video_source)
            self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        def get_frame(self):
            if self.vid.isOpened():
                ret, frame = self.vid.read()
                if ret:
                    return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                else:
                    return (ret, None)
            else:
                return (None, None)

    window = tkinter.Tk()
    App(window, 'Camera')
