"""
    Filename    :   conversions.py
    Description :   Part of EtherChainPy
    By          :   Emmanuel Adigun (emmanuel@zignal.net)
    Date        :   10 May 2022
"""
import json

class Conversions(object):
    """
    Conversion Module ...
    """
    def __init__(self, client=None):
        self.math_base = 10
        self.response = None
        self.client = client

    def to(self, what):
        w = what.upper()
        if w   == "WEI": return self.toWEI()
        elif w == "GWEI": return self.toGWEI()
        elif w == "ETH": return self.toETH()
        elif w == "ZAR": return self.toZAR()
        elif w == "USD": return self.toUSD()
        elif w == "EUR": return self.toEUR()
        else: return self.toJSON()

    def toJSON(self):
        if self.response: return self.response.json()
        else: return None

    
    def toWEI(self):
        wei = None
        if self.response:
            data = self.response.json()
            if "result" in data: 
                rd = data["result"]
                if isinstance(rd,str):
                    wei = int(data["result"],self.math_base)
                elif isinstance(rd,list):
                    wei = []
                    for r in rd: 
                        r.update({"wei": int(r["balance"],self.math_base) })
                        wei.append(r)

        return wei
    

    def toGWEI(self):
        gwei = None
        if self.response:
            data = self.response.json()
            if "result" in data: 
                rd = data["result"]
                if isinstance(rd,str):
                    gwei = int(data["result"],self.math_base)/(10**9)
                elif isinstance(rd,list):
                    gwei = []
                    for r in rd: 
                        r.update({"gwei": int(r["balance"],self.math_base)/(10**9) })
                        gwei.append(r)
        return gwei

    def toETH(self):
        eth = None
        if self.response:
            data = self.response.json()
            if "result" in data: 
                rd = data["result"]
                if isinstance(rd,str):
                    eth = int(data["result"],self.math_base) / (10**18)
                elif isinstance(rd,list):
                    eth = []
                    for r in rd: 
                        r.update({"eth": int(r["balance"],self.math_base)/(10**18) })
                        eth.append(r)
        
        return eth

    def toFIAT(self, value=None, to="ZAR"):
        fiat = None
        if self.client != None and value != None:
            params = {"fsym":"ETH", "tsyms":to.upper()}
            if self.client.conversion_api_key != None:
                params.update({"api_key":self.client.conversion_api_key})
            r = self.client.get(self.client.conversion_url,params).json()
            if to.upper() in r: 
                cv = float(r[to.upper()])
                if   isinstance(value,int): fiat = float(value) * cv
                if   isinstance(value,float): fiat = float(value) * cv
                elif isinstance(value,str): fiat = float(value) * cv
                elif isinstance(value,list):
                    fiat = []
                    for v in value:
                        a = v
                        a.update({to:float(v["eth"]) * cv})
                        fiat.append(a)

        return fiat


    def toZAR(self):
        v = self.toETH()  # base 
        return self.toFIAT(v, "ZAR")


    def toUSD(self):
        v = self.toETH()  # base 
        return self.toFIAT(v,"USD")

    def toEUR(self):
        v = self.toETH()  # base 
        return self.toFIAT(v,"EUR")






