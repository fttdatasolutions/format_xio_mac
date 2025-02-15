# format_xio_mac
Scripting mac address format transformation for Crestron XIO Cloud

I took a few minutes to script a transformation that I might have to make a lot, in the future. For importing asset data to a cloud configuration platform, AV equipment manufacturer Crestron wants to format equipment mac addresses in this format:

C4.42.68.xx.xx.xx

However, we record mac addresses with a barcode scanner using this format:

C44268xxxxxx

So, how do we add dots to separate the octets in a mac address? I addressed that and also accounted for mac addresses with hyphens separating the octets (C4-42-68-xx-xx-xx). The script takes a .csv file (I hard-coded a path and filename, where the file will be for users in my team), transforms a field named 'Mac Address,' and replaces the .csv file with the updated field.
