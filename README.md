# MTRX2700 Major Project

### Group 7

<p>Name:<br>
<ol>
	<li>Andrei Agnew</li>
	<li>Daniel Miu </li>
  <li>Mary Khreich </li>
	<li>Minghan Li  </li>
  <li>Xuechi Xiang </li>

### Barcodeless Scanning
<p>
To create a more futuristic supermarket experience, we have designed a barcodeless scanning checkout system that utilises object detection to add products to a customers’ receipt rather than scanning a barcode. There are two main modules that our system can be broken down into: the hardware system and the user interface.
</p>
  
<p>
The hardware system uses a Lidar sensor to scan an object from a fixed distance, compare the scan to pre-set data to determine the objects nature, and communicate this information to the user interface.
</p>
  
<p>
The user interface emulates a checkout register in that it shows a list of items that have been scanned,
the quantity of each, and their price. The UI will repeatedly call for an item to scan until the customer
chooses to checkout.
</p>
  
<p>
Additional functions are included to enhance the user experience such as displaying a ‘scanning’ message
on the microcontroller during the scan and playing different sounds depending on successful or unsuccessful
scans.
An extension that can be implemented if time allows is to create a UI mode to add objects to the list of
items that can be detected. The hardware will scan the new object and add the data to a text file. This
text file will then be used as the pre-set reference data when objects are scanned for checkout.
</p>


## Modules for the System

### Scanning 

### UI

The UI is created in python with the tkinter module. It essentially forms the core of this project as it sends the scan command to the dragon board, receives information about the detected object and outputs it in the form as a receipt. It also allows for the final checkout button, where the full receipt will be printed and an exit button is included to exit the program

#### Detailed Description

- The window is created using tkinters tk function to display the root window
	- This window is then customisable to our needs.
	- This customisation includes the screen width/height, the background colour, the layout of the screen, and widgets included

- For this UI, we only require a label for the title (being check), a table that keep tracks of the item detected for checkout, and 2 buttons for scanning and checkout
- Scan button sends a character to the serial port for the dragonboard to detect, in which will trigger the scanning process for the object detection function to use and determine what object is detected.
	- After the object detection function determines what object is detected, this will be returned and used to populate the receipt table
	- In which we can determine whether it is an unique item (item that hasn't been detected), or another quantity of an past item
- The checkout button will create a popup window that displays the full receipt of items scanned, and include an exit button where it'll exit the program.

### 