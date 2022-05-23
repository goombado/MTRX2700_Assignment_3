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
