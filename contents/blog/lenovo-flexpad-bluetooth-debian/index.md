---
title: Getting bluetooth to work on a Lenovo Ideapad Flex 2 running Debian Jessie
date: 2014-12-31
template: page.jade
comments: true
code: true
---

The Lenovo Ideapad Flex 2 actually works pretty nicely out of the box in Debian Jessie with the exception of wifi and bluetooth.
Wifi can be easily fixed by adding the non-free reposityory and installing the package ``broadcom-sta-dkms``.
The procedure of getting bluetooth working unfortunately is MUCH more involved.
During setting up bluetooth you are most likely to encounter the following problems in chronological order:

* You will not find the bluetooth device
* Linux will not find the bluetooth device
* Linux will not be able to initialize the bluetooth device
* Linux will forget about the device after suspend/resume
* You will not be able to connect to an audio device
* Bluetooth and wifi interfere

Let's fix this one by one.
The following guide applies to the Debian linux kernel version 3.16.
As there seems to be lot of fluctuations in the bluetooth kernel module,
you might want to check for your kernel version using ``uname -a``.
If you get something that looks like this

```
Linux debian 3.16.0-4-amd64 #1 SMP Debian 3.16.7-ckt2-1 (2014-12-08) x86_64 GNU/Linux
```

then you are ready to go.
This guide is largely based on [an existing guide][1], where an older kernel was used.
In the 3.16 kernel, things are somewhat easier as less patching needs to be done.

## Identifying the bluetooth device

The bluetooth adapter is connected via USB. ``lsusb`` tells us the following:

```
Bus 003 Device 002: ID 8087:8000 Intel Corp. 
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 005: ID 04f3:0446 Elan Microelectronics Corp. 
Bus 001 Device 003: ID 105b:e065  
Bus 001 Device 002: ID 174f:14b7 Syntek 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

Huh? No bluetooth device? Hmmm, but there is a mysterious unnamed device.
Let's gather a little bit more information using ``usb-devices``:

```
T:  Bus=01 Lev=01 Prnt=01 Port=05 Cnt=02 Dev#=  3 Spd=12  MxCh= 0
D:  Ver= 2.00 Cls=ff(vend.) Sub=01 Prot=01 MxPS=64 #Cfgs=  1
P:  Vendor=105b ProdID=e065 Rev=01.12
S:  Manufacturer=Broadcom Corp
S:  Product=BCM43142A0
S:  SerialNumber=485AB6C7AE1A
C:  #Ifs= 4 Cfg#= 1 Atr=e0 MxPwr=0mA
I:  If#= 0 Alt= 0 #EPs= 3 Cls=ff(vend.) Sub=01 Prot=01 Driver=btusb
I:  If#= 1 Alt= 0 #EPs= 2 Cls=ff(vend.) Sub=01 Prot=01 Driver=btusb
I:  If#= 2 Alt= 0 #EPs= 2 Cls=ff(vend.) Sub=ff Prot=ff Driver=(none)
I:  If#= 3 Alt= 0 #EPs= 0 Cls=fe(app. ) Sub=01 Prot=01 Driver=(none)
```

From the above output we can extract the most important information which is

* The device id 105b:e065
* The name of the adapter BCM43142A0

## Convince Linux that it can handle the bluetooth adapter

For reasons unbeknownst to me the BCM43142A0 adapter is in principle supported by the linux kernel
but still not recognized.
To remedy this, the following has to be done.

1) Check out the kernel source:

    apt-get source linux

The rest of the following instructions have to be performed inside the kernel source folder.

2) Add the following line to the the file ``<kernel-source>/drivers/btusb.c``:

    { USB_DEVICE(0x105b, 0xe065), .driver_info = BTUSB_BCM_PATCHRAM },

You can also do this using [this patch](btusb.patch) by running

```
patch -p1 < btusb.patch
```

3) Recompile and install the bluetooth module (run inside the linux source folder)

```
cp /lib/modules/$(uname -r)/build/Module.symvers ./
make oldconfig
make prepare
make modules_prepare
make modules SUBDIRS=drivers/bluetooth
sudo cp drivers/bluetooth/btusb.ko /lib/modules/$(uname -r)/kernel/drivers/bluetooth/btusb.ko
sudo depmod
```

4) Reload the newly compiled module

```
sudo modprobe -r btusb
sudo modprobe btusb
```

You can verify a successful completion of this procedure by looking at the ``dmesg`` output,
where you should find something along the lines of

```
[26861.031148] usbcore: deregistering interface driver btusb
[26863.881849] usbcore: registered new interface driver btusb
[26863.883344] bluetooth hci0: firmware: failed to load brcm/BCM43142A0-105b-e065.hcd (-2)
[26863.883348] bluetooth hci0: Direct firmware load failed with error -2
[26863.883350] bluetooth hci0: Falling back to user helper
[26863.884074] bluetooth: hci0: BCM: patch brcm/BCM43142A0-105b-e065.hcd not found
```

## Providing the firmware
From the dmesg output we can tell that the firmware for the device is not available,
which apparently is due to licensing restrictions.
The recommended way of obtaining the firmware is to grab it from a Windows installation
and convert it to the required hcd format.
To spare you this crazy procedure, here is the [converted and ready-to-use firmware](BCM43142A0-105b-e065.hcd).
As you might have guessed from the dmesg output it needs to end up in ``/lib/firmware/brcm/``.
You will have to create this directory yourself.
After reloading the bluetooth module a second time

```
sudo modprobe -r btusb
sudo modprobe btusb
```

this ``dmesg`` output should make you happy.

```
[28191.358773] usbcore: deregistering interface driver btusb
[28196.493087] usbcore: registered new interface driver btusb
[28196.493258] bluetooth hci0: firmware: direct-loading firmware brcm/BCM43142A0-105b-e065.hcd
[28196.497750] bluetooth: hci0: BCM: patching hci_ver=06 hci_rev=00ac lmp_ver=06 lmp_subver=210b
[28196.953017] bluetooth: hci0: BCM: firmware hci_ver=06 hci_rev=00ac lmp_ver=06 lmp_subver=210b
```

## Survive suspend/resume

Your bluetooth adapter should now be initialized automatically during booting.
It will however not yet survive an suspend/resume cycle.
As a remedy, simply put the line

```
SUSPEND_MODULES="$SUSPEND_MODULES btusb"
```

into ``/etc/pm/config.d/btusb``.
This reloads the bluetooth module during resume.

## Get audio working

I was quite surprised to find that it is not possible to connect to audio devices in Debian out of the box.
In order to enable it, run

```
sudo apt-get install pulseaudio-module-bluetooth
pulseaudio -k
```

## Solve interference problem

I found that the quality of the bluetooth audio transmission highly depends
on the amount of data currently being sent over wifi.
When I turn off wifi, audio output is crystal clear.
During heavy downloads, I get skipping audio.
There seems to be some [interference][2] between the two adapters.
I imagine that the Windows driver somehow accounts for this,
by employing frequency hopping or something similar,
but I currently have no clue how to get this feat accomplished under linux.
Any help in this respect is appreciated.

[1]: http://dhanar10.blogspot.co.at/2014/05/bcm43142-bluetooth-getting-it-to-work.html
[2]: http://en.wikipedia.org/wiki/Electromagnetic_interference_at_2.4_GHz#Bluetooth

