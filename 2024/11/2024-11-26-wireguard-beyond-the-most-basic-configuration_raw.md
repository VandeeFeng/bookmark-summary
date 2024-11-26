Title: Wireguard: Beyond the most basic configuration

URL Source: https://sloonz.github.io/posts/wireguard-beyond-basic-configuration/

Published Time: 2024-06-28T00:00:00Z

Markdown Content:
Last week I wanted to replace my OpenVPN setup with WireGuard. The basics were well-documented, going beyond the basics was a bit trickier. Let me teach you want I learned.

The basics
----------

But first, let’s summarize the basics. I have a server with a hosting provider that I want to use as a VPN server. I won’t delve into details here, since there are so many great explanations on the web already ([here](https://www.wireguard.com/quickstart/#nat-and-firewall-traversal-persistence), [here](https://www.wireguard.com/netns/), [here](https://volatilesystems.org/wireguard-in-a-separate-linux-network-namespace.html) or [here](https://wiki.archlinux.org/title/WireGuard)), let’s just make a quick summary of a simple setup, as a base for discussing the (slightly) more advanced usages I had to configure myself:

1.  Generate a keypair (private key/public key) for the server.
    
2.  Generate a keypair (private key/public key) for each client.
    
3.  Pick a network for the VPN (for me: `10.100.0.0/16`), an IP for the server (`10.100.0.1`) and the clients (`10.100.0.2`, `10.100.0.3`, etc.)
    
4.  Create the configuration for the server
    

```
[Interface]
Address = 10.100.0.1/24
PrivateKey = (redacted)
ListenPort = 51820
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -A FORWARD -o %i -j ACCEPT; iptables -t nat -A POSTROUTING -o ens0 -j MASQUERADE
PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -D FORWARD -o %i -j ACCEPT; iptables -t nat -D POSTROUTING -o ens0 -j MASQUERADE

[Peer]
PublicKey = (redacted)
AllowedIPs = 10.100.0.2/32

[Peer]
PublicKey = (redacted)
AllowedIPs = 10.100.0.3/32
```

5.  Start the server, `wg up /etc/wireguard/wg0.conf`
    
6.  Create the configuration for the client
    

```
[Interface]
PrivateKey = (redacted)

[Peer]
PublicKey = (redacted)
Endpoint = my-server.example.com:51820
AllowedIPs = 0.0.0.0/0, ::/0
```

7.  Start the client: `wg up /etc/wireguard/wg0.conf`

(optionally, not pictured here: create a network namespace for your VPN, so your main connection still has a direct access to the internet, but you can put applications that want the VPN in the VPN network namespace).

NAT
---

Some applications (looking at you, BitTorrent client) do not play well behind a NAT. Unfortunately, your VPN (wireguard or not) acts as a NAT. One widely used method to work around those issues is UPnP.

UPnP solves two issues:

*   Your computer does not know its public address on the internet (from the point of view of an external system) ; behind a VPN, you public address is the address of the VPN server, not the address assigned to you by your ISP (your VPN software knows that address — but the rest of the system generally has absolutely no knowledge of it). And if that address is not known by your peer-to-peer software, it cannot communicate it to other peers.
    
*   Even if that address is known and correctly communicated to a peer, if you listen to a port (for example, TCP 8043), the peer will try to reach you on that port, but on your VPN server IP. For that connection to actually reach your computer, your VPN software will have to set up a port forwarding rule (from VPN server 8043 to your ISP-assigned IP address, port 8043 — in a real setup, the two ports may actually differ, but let’s keep it simple for that explanation). UPnP provides a way to do that.
    

Let’s show that (obviously) our simple WireGuard-based VPN setup does not provide UPnP (`external-ip` is a tool provided by `miniupnpc`, an UPnP client):

```
$ external-ip
No IGD UPnP Device found on the network !
```

That was expected. Wireguard, being a very simple kernel module, does not come with batteries included in the form of a UPnP server. We will have to do it manually. Thankfully, it is pretty straightforward:

1.  Install `miniupnpd` (on the server, obviously).
    
2.  Configure `miniupnpd`.
    
3.  Add `PostUp = systemctl start miniupnpd` and `PostDown = systemctl stop miniupnpd` in your wireguard configuration file.
    

The only non-trivial step here is configuring `miniupnpd`. All the action lies in `/etc/miniupnpd/miniupnpd.conf`. Here is what you have to configure:

*   `ext_ifname=ens0`: this is the internet-facing interface of your server (it may be different from `ens0`).
    
*   `listening_ip=wg0`: this is the wireguard network interface on your server.
    
*   `uuid=06df7440-dbac-404c-9c07-0b0dbfca609e`: use `uuidgen` to generate one. Or you can steal mine, it doesn’t matter, since everything happens in a private, non-routable network.
    
*   `allow 1024-65535 10.100.0.0/16 1024-65535`: this is where you specify your wireguard network (in my basic setup `10.100.0.0/16`).
    

Let’s check that it works:

```
$ external-ip
(redacted, but it correctly returned my server IP)
$ upnpc -n 10.100.0.2 8043 8043 tcp 300
external (redacted:server-ip):8043 TCP is redirected to internal 10.100.0.2:8043 (duration=300)
$ socat TCP-LISTEN:8043 STDIO
```

And on another machine:

```
$ socat TCP:(redacted:server-ip):8043 STDIO
```

You can see that the two `socat` instances can communicate with each other, passing through your VPN.

IPv6
----

You know what’s even better than supporting UPnP to work around the issues introduced that NAT ? Not having NAT. And the good news is, with IPv6, you actually can.

The few tutorials who actually explains how to setup IPv6 for a WireGuard-based VPN usually mirror the IPv4 setup: assign a private, non-routable network to it (`10.100.0.0/16` for IPv4 get translated to something like `fd00:dead:beef::/48` for IPv6), assign IP addresses in this network to the server and the clients, and add an `ip6tables` masquerade action.

We’re not going to do that. We can do better, and we will do better.

The first thing to notice is that my hosting provider has assigned to me a whole /48 network for my account (`2001:aaaa:bbbb::/48`), and a /56 (`2001:aaaa:bbbb:1000::1/56`) for my server. We can take advantage of that to assign different publicly routable IPv6 addresses to our clients, instead of assigning private, non-routable addresses.

Let’s start with the server configuration. Let’s add IPv6. We assign the /80 subnetwork `2001:aaaa:bbbb:1000:cafe::/80` to VPN network. I’ll only list added configuration lines, not repeating existing ones:

```
[Interface]
Address = 2001:aaaa:bbbb:1000:cafe::1/80

[Peer]
AllowedIPs = 2001:aaaa:bbbb:1000:cafe::2/128

[Peer]
AllowedIPs = 2001:aaaa:bbbb:1000:cafe::3/128
```

Client-side, this is not much more complicated:

```
[Interface]
Address = 2001:aaaa:bbbb:1000:cafe::2/128
```

Just one sanity check: on your server, `ip -6 route get 2001:aaaa:bbbb:1000:cafe::2` must return the WireGuard interface (`wg0`). If not, you will have to give a lower metric to `wg0` in your routes. But you can now, on your client, directly listen to a port:

```
$ socat TCP6-LISTEN:8043
```

and it will be accessible from the public internet without any UPnP setup:

```
$ socat TCP6:[2001:aaaa:bbbb:1000:cafe::2]:8043
```

Also, the IP address on the device of your default route will be `2001:aaaa:bbbb:1000:cafe::2`, meaning no need for UPnP to dectect your public, routable IPv6: your VPN interface IP (which is private in the IPv4 case, but now public for IPv6) is also your public IP.
