# BUILD GUIDE FOR TAO TE CHING <br>

## Intro:
<h4>Okay, now you have your PCB and components in hand and are ready to build it! I've tried to make this guide as comprehensive as possible, but you are free to improve it and submit a PR to this repo. </h4>
<br>

## Tools Required
- Soldering iron
- Solder
- Tweezers
- Flux (recommended)
- USB cable
- Multimeter (optional but helpful)

<br>

## Recommended Build Order
1. Solder diodes
2. Solder hotswap sockets
3. Solder MCU
4. Install switches
5. Flash firmware
6. Test the matrix

<br>

## Diodes
<h4>
N.T: Match the stripe on the diode with the line on the PCB silkscreen. The stripe indicates the cathode. If the diode is reversed the keyboard matrix will not work. <br><br>

Firstly tin one of the pads of the diodes, then using tweezers hold the diodes down and then melt the solder and hold it. In the end it should look something like this: </h4>
<br>
<div align="center">
<img alt="image" height="256" src="https://cdn.hackclub.com/019cf4cc-8022-75f0-b38f-64fa62f0c22e/image.png" />
</div>

## HotSwap Sockets
<h4> N.T: I have used TTC Pokayoke Hotswap Sockets V2 which are compatible with Kailh socket footprints and are reversable. If you have used Kailh or any other sockets which are NOT reversible please pay attention to the orientation as it can cause problems later down the line while snapping in the plate. <br><br>

I recommend not tinning the pads before putting the sockets in. So you just want to place the sockets in the hole and align it with the footprint. Now you want to add solder to the pads. Keep the solder molten and switch to your tweezers to now put pressure on the socket so it sits flush. Now after it has solidified, solder the other pad too. Now! It should look like this: </h4>
<div align="center">
<img alt="image" height="256" src="https://cdn.hackclub.com/019cf4d0-5b2e-7005-a8d0-68bf43ea5019/image.png" />
</div>
<br>

## MCU
<h4> For the Tao Te Ching keyboard I used the <b>XIAO RP2350</b>. Make sure the MCU is oriented correctly before soldering it to the PCB. Incorrect orientation may prevent the keyboard from functioning or could damage the board. <br><br>

First place the MCU onto the footprint and ensure that all pins line up properly with the pads on the PCB. Once aligned, you may want to temporarily secure the board with a small piece of tape or hold it in place while soldering. <br><br>

Begin by soldering <b>one corner pin</b>. After this, check that the MCU sits flat against the PCB and that all pins are aligned correctly. If necessary, reheat the solder joint and adjust the position of the MCU. <br><br>

Once you are satisfied with the alignment, proceed to solder the remaining pins. Take your time and make sure each pin is properly connected to its pad. <br><br>

After soldering, visually inspect the pins to ensure there are <b>no solder bridges</b> between them.
</h4>
<div align="center">
<img alt="image" height="256" src="https://cdn.hackclub.com/019cf4ee-d7da-7aaf-abc4-7c442575ab7f/image.png" />
</div>
<br>

## Switches:
<h4>
  For the switches you can just press the switches into the plate and then align the plate with the PCB and HotSwap sockets and just push them in column by column. Theres not much to do here!
</h4> <br>

## Firmware: 
While pressing down the boot button on your MCU plug it in, wait till a drive pops up. Get the circuitpython uf2 from [HERE](https://circuitpython.org/board/seeeduino_xiao_rp2350/). <br> <br>
Add /kmk from the kmk library from [HERE](https://github.com/KMKfw/kmk_firmware) to the drive that appears. <br> <br> Now get the code from [/firmware](firmware) and add it to the respective MCUs.

## AND YOU ARE DONE!!!
