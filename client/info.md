

支持Windows/OS X/Linux

平台不同 用的方法也不同

Windows 使用Wmi

採集各硬體信息範例    
https://www.activexperts.com/admin/scripts/wmi/python/



Module

- Windows

    ```
    wmi
    win32
    ```

- Linux

    ```
    paramiko
    salt
    ```


Node


- agent

    本地採集資產
    ```
    shell command
    ```
    
    
- ssh
    
    僅支持遠程採集資產，必須有主機名
    ```
    paramiko
    ```
    


- salt

    僅支持遠程採集資產，必須有主機名
    ```
    
    ```





Linux

- memory

    dmidecode -t memory
    
    https://www.unixmen.com/getting-complete-hardware-specification-linux-terminal-using-facter-dmidecode/
    https://www.2daygeek.com/easy-ways-to-check-size-of-physical-memory-ram-in-linux/
    https://www.unixmen.com/getting-complete-hardware-specification-linux-terminal-using-facter-dmidecode/
    http://www.gkhan.in/how-to-identify-virtual-server-or-physical-server/

- Disk

    ```
    sudo /sbin/fdisk -l|grep Disk|egrep -v 'identifier|mapper|Disklabel'
    
    >>>
    Disk /dev/sda: 10 GiB, 10737418240 bytes, 20971520 sectors
    Disk /dev/sdb: 80 GiB, 85899345920 bytes, 167772160 sectors
    ```
    
    ```
    sudo hdparm -i /dev/sda | grep Model
    
    >>>
    Model=VBOX HARDDISK, FwRev=1.0, SerialNo=VB86f09477-08304f68
    ```
    
    
    




目錄結構

```
client
│
├─bin 執行目錄
├─conf 設定檔
├─core
├─lib 公共區(重複代碼)
├─log 日誌
├─src 業務邏輯，
└─test
```


test1



