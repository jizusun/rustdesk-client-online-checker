# RustDeskOnlinestat
This describes how you can easily read the onlinestatus of your rustdesk clients from your selfhosted Rustdesk servers



Hey, 

with the help of ChatGPT and Wireshark I have managed to monitor the onlinestate of the clients connected to my HBBS.

In case my scripts don't work for you (because I didn't manage to identify if there are server specific packets sent) I will describe what I have done. I hope to be n00b-save.

First I installed wireshark and opened it with administrative rights. Wireshark needs admin/root-permissions to listen to the network traffic. Then I selected the networkcard where my internet traffic is going through (or the traffic that goes to your rustdesk-server). 

That was the moment everything went totally bonkers. But don't be alarmed we will fix that.

In the upper half there is a filter-textbox. Write: ip.addr ==  IP.OF.YOUR.RUSTDESK.SERVER

That is the moment when only your rustdesk-traffic will be shown. At this moment I made an attempt to connect to an offline client and to one online client (so ChatGPT can identify the return messages of the server in the packets).

Now stop Wireshark (stopbutton most left in the icons above the filter box).

Select all packets in the list.

Go to File => export packetdissection => plain text

Now go to ChatGPT, upload the file and ask hin to analyse the traffic in the file and explain the main communication to you. ChatGPT will identify your ID and the ID's you were connecting to. 

And it can identify the answers of the server to you. Now you have everything you need to make ChatGPT write you a script to check the onlinestate of your ID's.

I have put two scripts in this repository (PHP and python) that ChatGPT gave me. 

Please change the serverIP in both scripts to your rustdesk server IP. I'd recommend to set the sourceId to some random number with 9 digits and the targetId is the ID you want to check. Now let the magic happen and check the online stat of your rustdesk clients without being pro subscriber. 

Btw. If you want to build your own addressbook without having pro:

RustDesk accepts URL handlers like this:

rustdesk://123456789

Clicking a link of this schematic it will connect to the client with that ID.

Hope this helps some people.
