# APITracker

APITracker is a major update to our tool **Malpimp**. It follows the same methodology for hooking and reporting but with an enhanced feature set and more stable logging options.

### New to APITracker: 

1. **Server Logging:** APItracker can send the API logs on the remote server so you don’t have to worry about ransomewares, etc.

2. **Parameters:** APItracker can also report the API parameters in a dynamic approach. We can change the number of parameters as per our requirements.

3. **Heap Only logging:** APITracker support heap only logging, it means by enabling the logheap option in config file it will only report the API calls that are coming from heap region. It is useful in malware unpacking and shellcode analysis.

4. **Modules Logging:** Now we can log API calls from the selected modules. For example, in case of DLL analysis we want to log the calls only from DLL not from rundll binary, so this option is a great help when we want to log the APIs only from some specific modules.

> More info at : https://cysinfo.com/apitracker-windows-api-tracing-tool/
