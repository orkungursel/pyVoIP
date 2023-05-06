from pyVoIP.SIP import SIPMessage
import pytest


@pytest.mark.parametrize(
    "packet,expected",
    [
        (
            b"""INVITE sip:bob@biloxi.com SIP/2.0\r\nVia: SIP/2.0/UDP pc33.atlanta.com;branch=z9hG4bK776asdhds\r\nMax-Forwards: 70\r\nTo: Bob <sip:bob@biloxi.com>\r\nFrom: Alice <sip:alice@atlanta.com>;tag=1928301774\r\nCall-ID: a84b4c76e66710@pc33.atlanta.com\r\nCSeq: 314159 INVITE\r\nContact: <sip:alice@pc33.atlanta.com>\r\nContent-Type: application/sdp\r\nContent-Length: 142\r\n\r\n""",
            {
                "Via": [
                    {
                        "type": "SIP/2.0/UDP",
                        "address": ("pc33.atlanta.com", 5060),
                        "branch": "z9hG4bK776asdhds",
                    },
                ],
                "Max-Forwards": 70,
                "To": {
                    "raw": "Bob <sip:bob@biloxi.com>",
                    "tag": "",
                    "uri": "sip:bob@biloxi.com",
                    "uri-type": "sip",
                    "user": "bob",
                    "password": "",
                    "display-name": "Bob",
                    "host": "biloxi.com",
                    "port": 5060,
                },
                "From": {
                    "raw": "Alice <sip:alice@atlanta.com>;tag=1928301774",
                    "tag": "1928301774",
                    "uri": "sip:alice@atlanta.com",
                    "uri-type": "sip",
                    "user": "alice",
                    "password": "",
                    "display-name": "Alice",
                    "host": "atlanta.com",
                    "port": 5060,
                },
                "Call-ID": "a84b4c76e66710@pc33.atlanta.com",
                "CSeq": {"check": 314159, "method": "INVITE"},
                "Contact": {
                    "raw": "<sip:alice@pc33.atlanta.com>",
                    "tag": "",
                    "uri": "sip:alice@pc33.atlanta.com",
                    "uri-type": "sip",
                    "user": "alice",
                    "password": "",
                    "display-name": "",
                    "host": "pc33.atlanta.com",
                    "port": 5060,
                },
                "Content-Type": "application/sdp",
                "Content-Length": 142,
            },
        ),
        (
            b"""ACK sip:bob@biloxi.com SIP/2.0\r\nVia: SIP/2.0/UDP pc33.atlanta.com;branch=z9hG4bKkjshdyff\r\nTo: Bob <sip:bob@biloxi.com>;tag=99sa0xk\r\nFrom: Alice <sip:alice@atlanta.com>;tag=88sja8x\r\nMax-Forwards: 70\r\nCall-ID: 987asjd97y7atg\r\nCSeq: 986759 ACK\r\n\r\n""",
            {
                "Via": [
                    {
                        "type": "SIP/2.0/UDP",
                        "address": ("pc33.atlanta.com", 5060),
                        "branch": "z9hG4bKkjshdyff",
                    },
                ],
                "To": {
                    "raw": "Bob <sip:bob@biloxi.com>;tag=99sa0xk",
                    "tag": "99sa0xk",
                    "uri": "sip:bob@biloxi.com",
                    "uri-type": "sip",
                    "user": "bob",
                    "password": "",
                    "display-name": "Bob",
                    "host": "biloxi.com",
                    "port": 5060,
                },
                "From": {
                    "raw": "Alice <sip:alice@atlanta.com>;tag=88sja8x",
                    "tag": "88sja8x",
                    "uri": "sip:alice@atlanta.com",
                    "uri-type": "sip",
                    "user": "alice",
                    "password": "",
                    "display-name": "Alice",
                    "host": "atlanta.com",
                    "port": 5060,
                },
                "Max-Forwards": 70,
                "Call-ID": "987asjd97y7atg",
                "CSeq": {"check": 986759, "method": "ACK"},
            },
        ),
        (
            b"BYE sip:alice@pc33.atlanta.com SIP/2.0\r\nVia: SIP/2.0/UDP 192.0.2.4;branch=z9hG4bKnashds10\r\nMax-Forwards: 70\r\nFrom: Bob <sip:bob@biloxi.com>;tag=a6c85cf\r\nTo: Alice <sip:alice@atlanta.com>;tag=1928301774\r\nCall-ID: a84b4c76e66710\r\nCSeq: 231 BYE\r\nContent-Length: 0\r\n\r\n",
            {
                "Via": [
                    {
                        "type": "SIP/2.0/UDP",
                        "address": ("192.0.2.4", 5060),
                        "branch": "z9hG4bKnashds10",
                    },
                ],
                "Max-Forwards": 70,
                "From": {
                    "raw": "Bob <sip:bob@biloxi.com>;tag=a6c85cf",
                    "tag": "a6c85cf",
                    "uri": "sip:bob@biloxi.com",
                    "uri-type": "sip",
                    "user": "bob",
                    "password": "",
                    "display-name": "Bob",
                    "host": "biloxi.com",
                    "port": 5060,
                },
                "To": {
                    "raw": "Alice <sip:alice@atlanta.com>;tag=1928301774",
                    "tag": "1928301774",
                    "uri": "sip:alice@atlanta.com",
                    "uri-type": "sip",
                    "user": "alice",
                    "password": "",
                    "display-name": "Alice",
                    "host": "atlanta.com",
                    "port": 5060,
                },
                "Call-ID": "a84b4c76e66710",
                "CSeq": {"check": 231, "method": "BYE"},
                "Content-Length": 0,
            },
        ),
        (
            b"CANCEL sip:123456789@sample.pstn.ie1.twilio.com SIP/2.0\r\nCSeq: 969240 CANCEL\r\nCall-ID: 284466\r\nFrom: <sip:test@sample.pstn.ie1.twilio.com>;tag=168502\r\nTo: <sip:123456789@sample.pstn.ie1.twilio.com>\r\nVia: SIP/2.0/TCP 192.168.61.4:61244;branch=z9hG4bK847573\r\nContent-Length: 0\r\n\r\n",
            {
                "Via": [
                    {
                        "type": "SIP/2.0/TCP",
                        "address": ("192.168.61.4", 61244),
                        "branch": "z9hG4bK847573",
                    },
                ],
                "CSeq": {"check": 969240, "method": "CANCEL"},
                "Call-ID": "284466",
                "From": {
                    "raw": "<sip:test@sample.pstn.ie1.twilio.com>;tag=168502",
                    "tag": "168502",
                    "uri": "sip:test@sample.pstn.ie1.twilio.com",
                    "uri-type": "sip",
                    "user": "test",
                    "password": "",
                    "display-name": "",
                    "host": "sample.pstn.ie1.twilio.com",
                    "port": 5060,
                },
                "To": {
                    "raw": "<sip:123456789@sample.pstn.ie1.twilio.com>",
                    "tag": "",
                    "uri": "sip:123456789@sample.pstn.ie1.twilio.com",
                    "uri-type": "sip",
                    "user": "123456789",
                    "password": "",
                    "display-name": "",
                    "host": "sample.pstn.ie1.twilio.com",
                    "port": 5060,
                },
                "Content-Length": 0,
            },
        ),
        (
            b"""REGISTER sip:127.0.0.1 SIP/2.0\r\nVia: SIP/2.0/UDP 127.0.0.1:5059;branch=z9hG4bK30af91ecac014a5b957bcb607;rport\r\nFrom: "pass" <sip:pass@127.0.0.1>;tag=85147370\r\nTo: "pass" <sip:pass@127.0.0.1>\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@127.0.0.1:5059\r\nCSeq: 1 REGISTER\r\nContact: <sip:pass@127.0.0.1:5059;transport=UDP>;+sip.instance="<urn:uuid:5BEB99C2-D319-4B2C-8BD3-6F71796E9E07>"\r\nAllow: INVITE, ACK, BYE, CANCEL, OPTIONS\r\nMax-Forwards: 70\r\nAllow-Events: org.3gpp.nwinitdereg\r\nUser-Agent: pyVoIP 2.0.0\r\nExpires: 120\r\nContent-Length: 0\r\n\r\n""",
            {
                "Via": [
                    {
                        "type": "SIP/2.0/UDP",
                        "address": ("127.0.0.1", 5059),
                        "branch": "z9hG4bK30af91ecac014a5b957bcb607",
                        "rport": None,
                    }
                ],
                "From": {
                    "raw": '"pass" <sip:pass@127.0.0.1>;tag=85147370',
                    "tag": "85147370",
                    "uri": "sip:pass@127.0.0.1",
                    "uri-type": "sip",
                    "user": "pass",
                    "password": "",
                    "display-name": "pass",
                    "host": "127.0.0.1",
                    "port": 5060,
                },
                "To": {
                    "raw": '"pass" <sip:pass@127.0.0.1>',
                    "tag": "",
                    "uri": "sip:pass@127.0.0.1",
                    "uri-type": "sip",
                    "user": "pass",
                    "password": "",
                    "display-name": "pass",
                    "host": "127.0.0.1",
                    "port": 5060,
                },
                "Call-ID": "6b86b273ff34fce19d6b804eff5a3f57@127.0.0.1:5059",
                "CSeq": {"check": 1, "method": "REGISTER"},
                "Contact": {
                    "raw": '<sip:pass@127.0.0.1:5059;transport=UDP>;+sip.instance="<urn:uuid:5BEB99C2-D319-4B2C-8BD3-6F71796E9E07>"',
                    "tag": "",
                    "uri": "sip:pass@127.0.0.1:5059",
                    "uri-type": "sip",
                    "user": "pass",
                    "password": "",
                    "display-name": "",
                    "host": "127.0.0.1",
                    "port": 5059,
                },
                "Allow": ["INVITE", "ACK", "BYE", "CANCEL", "OPTIONS"],
                "Max-Forwards": 70,
                "Allow-Events": "org.3gpp.nwinitdereg",
                "User-Agent": "pyVoIP 2.0.0",
                "Expires": 120,
                "Content-Length": 0,
            },
        ),
        # TODO: OPTIONS
        # TODO: INFO
        (
            b"""SUBSCRIBE sip:pass@127.0.0.1 SIP/2.0\r\nVia: SIP/2.0/UDP 127.0.0.1:5059;branch=z9hG4bK24bb16adff7945d1a7b0da37c;rport\r\nFrom: "pass" <sip:pass@127.0.0.1>;tag=46c3691d\r\nTo: <sip:pass@127.0.0.1>\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@0.0.0.0:5060\r\nCSeq: 1 SUBSCRIBE\r\nContact: <sip:pass@127.0.0.1:5059;transport=UDP>;+sip.instance="<urn:uuid:673FA933-7448-440B-AE08-969D75EB7AC3>"\r\nMax-Forwards: 70\r\nUser-Agent: pyVoIP 2.0.0\r\nExpires: 240\r\nEvent: message-summary\r\nAccept: application/simple-message-summary\r\nContent-Length: 0\r\n\r\n""",
            {
                "Via": [
                    {
                        "type": "SIP/2.0/UDP",
                        "address": ("127.0.0.1", 5059),
                        "branch": "z9hG4bK24bb16adff7945d1a7b0da37c",
                        "rport": None,
                    }
                ],
                "From": {
                    "raw": '"pass" <sip:pass@127.0.0.1>;tag=46c3691d',
                    "tag": "46c3691d",
                    "uri": "sip:pass@127.0.0.1",
                    "uri-type": "sip",
                    "user": "pass",
                    "password": "",
                    "display-name": "pass",
                    "host": "127.0.0.1",
                    "port": 5060,
                },
                "To": {
                    "raw": "<sip:pass@127.0.0.1>",
                    "tag": "",
                    "uri": "sip:pass@127.0.0.1",
                    "uri-type": "sip",
                    "user": "pass",
                    "password": "",
                    "display-name": "",
                    "host": "127.0.0.1",
                    "port": 5060,
                },
                "Call-ID": "6b86b273ff34fce19d6b804eff5a3f57@0.0.0.0:5060",
                "CSeq": {"check": 1, "method": "SUBSCRIBE"},
                "Contact": {
                    "raw": '<sip:pass@127.0.0.1:5059;transport=UDP>;+sip.instance="<urn:uuid:673FA933-7448-440B-AE08-969D75EB7AC3>"',
                    "tag": "",
                    "uri": "sip:pass@127.0.0.1:5059",
                    "uri-type": "sip",
                    "user": "pass",
                    "password": "",
                    "display-name": "",
                    "host": "127.0.0.1",
                    "port": 5059,
                },
                "Max-Forwards": 70,
                "User-Agent": "pyVoIP 2.0.0",
                "Expires": 240,
                "Event": "message-summary",
                "Accept": "application/simple-message-summary",
                "Content-Length": 0,
            },
        ),
        (
            b"MESSAGE sip:456@127.0.0.1 SIP/2.0\r\nVia: SIP/2.0/UDP 127.0.0.1:5059;branch=bb\r\nMax-Forwards: 70\r\nTo: <sip:456@127.0.0.1>\r\nFrom: <sip:pass@127.0.0.1>;tag=113bdaff\r\nCall-ID: cc\r\nCSeq: 1 MESSAGE\r\nAllow: INVITE, ACK, BYE, CANCEL, OPTIONS\r\nContent-Type: text/plain\r\nContent-Length: 3\r\n\r\n789",
            {
                "Via": [
                    {
                        "type": "SIP/2.0/UDP",
                        "address": ("127.0.0.1", 5059),
                        "branch": "bb",
                    },
                ],
                "Max-Forwards": 70,
                "To": {
                    "raw": "<sip:456@127.0.0.1>",
                    "tag": "",
                    "uri": "sip:456@127.0.0.1",
                    "uri-type": "sip",
                    "user": "456",
                    "password": "",
                    "display-name": "",
                    "host": "127.0.0.1",
                    "port": 5060,
                },
                "From": {
                    "raw": "<sip:pass@127.0.0.1>;tag=113bdaff",
                    "tag": "113bdaff",
                    "uri": "sip:pass@127.0.0.1",
                    "uri-type": "sip",
                    "user": "pass",
                    "password": "",
                    "display-name": "",
                    "host": "127.0.0.1",
                    "port": 5060,
                },
                "Call-ID": "cc",
                "CSeq": {"check": 1, "method": "MESSAGE"},
                "Allow": ["INVITE", "ACK", "BYE", "CANCEL", "OPTIONS"],
                "Content-Type": "text/plain",
                "Content-Length": 3,
            },
        ),
    ],
)
def test_sip_headers(packet, expected):
    message = SIPMessage(packet)
    assert message.headers == expected
