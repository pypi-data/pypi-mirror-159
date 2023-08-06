from inspect import trace
import tkinter
import tkinter.ttk


import threading
import queue

class quickGui:

    #region create

    def prv_createSpinbox(self, parent, __name, __value):
        tracer = tkinter.IntVar()

        v = tkinter.ttk.Spinbox(parent, textvariable=tracer, from_=-1000, to=1000)
        v.set(__value)
        def onChange(name, index, mode, tr=tracer, outSet = self.prv_outSet, outDict = self.prv_outDict, __name=__name):
            outDict[__name] = tr.get()
            outSet.add(__name)

        tracer.trace("w", onChange)

        self.prv_tracers.append(tracer)
        return v

    def prv_createEntry(self, parent, __name, __value):
        tracer = tkinter.StringVar()

        v = tkinter.ttk.Entry(parent, textvariable=tracer)
        v.delete(0, tkinter.END)
        v.insert(0, __value)

        def onChange(name, index, mode, tr=tracer, outSet = self.prv_outSet, outDict = self.prv_outDict, __name=__name):
            outDict[__name] = tr.get()
            outSet.add(__name)

        tracer.trace("w", onChange)

        self.prv_tracers.append(tracer)
        return v

    def prv_createButton(self, parent, __name, __value):
        v = tkinter.ttk.Button(parent, text = "press", command = __value)
        return v

    prv_createMap = {
        "int" : prv_createSpinbox,
        "float" : prv_createSpinbox,
        "str" : prv_createEntry,
        "function" : prv_createButton
    }

    #endregion

    #region update

    def prv_updateSpinbox(self, trinket, __value):
        trinket.set(__value)

    def prv_updateEntry(self, trinket, __value):
        trinket.delete(0, tkinter.END)
        trinket.insert(0, __value)

    def prv_updateButton(self, trinket, __value):
        pass

    prv_updateMap = {
        "int" : prv_updateSpinbox,
        "float" : prv_updateSpinbox,
        "str" : prv_updateEntry,
        "function" : prv_updateButton
    }

    #endregion

    def __init__(self, updateFrequency = 60) -> None:
        self.prv_inpQueue = queue.Queue()
        self.prv_outSet = set()
        self.prv_outDict = dict()

        self.prv_updateTime = int(1000/updateFrequency)
        
        if self.prv_updateTime < 1:
            self.prv_updateTime = 1

        self.prv_thread = threading.Thread(target=self.prv_runWindow, args=(self.prv_inpQueue, self.prv_outSet, self.prv_outDict, self.prv_updateTime), daemon=True)
        self.prv_thread.start()

        self.prv_trinkets = {}
        self.prv_tracers = []
        self.prv_running = True


    def prv_runWindow(self, inpQueue, outSet, outDict, updTime):
        self.prv_trinkets = {}
        self.prv_tracers = []
        
        self.prv_updateTime = updTime

        self.prv_index = 0
        self.prv_window = tkinter.Tk()

        self.prv_window.title("quickGui window")
        self.prv_inpQueue = inpQueue
        self.prv_outSet = outSet
        self.prv_outDict = outDict

        self.prv_frame = tkinter.ttk.Frame(self.prv_window)

        self.prv_frame.after(self.prv_updateTime, self.prv_handleElement)
        self.prv_window.mainloop()

    def prv_handleElement(self):
        if self.prv_inpQueue.empty() != True:
            __name, __value = self.prv_inpQueue.get()

            if __name not in self.prv_trinkets:

                if type(__value).__name__ in self.prv_createMap:
                    trinket = self.prv_createMap[type(__value).__name__](self, self.prv_window, __name, __value)
                else:
                    trinket = (tkinter.ttk.Label, "text")

                self.prv_trinkets[__name] = (
                    tkinter.ttk.Label(self.prv_window, text=__name),
                    trinket
                )

                self.prv_trinkets[__name][0].grid(column= 0, row=self.prv_index, padx = 20, pady = 5)
                self.prv_trinkets[__name][1].grid(column= 1, row=self.prv_index)
                self.prv_index += 1

            else:
                if type(__value).__name__ in self.prv_updateMap:
                    self.prv_updateMap[type(__value).__name__](self, self.prv_trinkets[__name][1], __value)
        
        self.prv_frame.after(self.prv_updateTime, self.prv_handleElement)

    def __setattr__(self, __name: str, __value: any) -> None:
        if __name[0] != "_" and  "prv_" not in __name:
            if "prv_running" in self.__dict__:
                if __name not in self.prv_trinkets:
                    #create trinket
                    self.prv_inpQueue.put((__name, __value))
                else:
                    if type(__value) != type(self.__dict__[__name]):
                        raise TypeError( "can't change type of displayed variable\n" +
                            str(type(__value)) + " is incompatible with " + str(type(self.__dict__[__name])))

                    #update value
                    self.prv_inpQueue.put((__name, __value))
                    pass

        super().__setattr__(__name, __value)

    def __getattribute__(self, __name: str) -> any:
        if __name[0] != "_" and  "prv_" not in __name:
            if "prv_running" in self.__dict__:
                if __name in self.prv_outSet:
                    self.__dict__[__name] = self.prv_outDict[__name]
                    self.prv_outSet.remove(__name)

        return super().__getattribute__(__name)