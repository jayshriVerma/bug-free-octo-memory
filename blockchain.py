import hashlib

class blockCoin:

	def __init__(self, prevblock_hash, transact_list):
		self.prevblock_hash = prevblock_hash
		self.transact_list = transact_list

		self.blockData = "-".join(transact_list) + "-" + prevblock_hash
		self.block_hash = hashlib.sha256(self.blockData.encode()).hexdigest()

#transact_list
s1="Meera sends 67 pound to yash"
s2="Leena sends 45 pound to deep"
s3="Rajveer sends 4.5 pound to kaira"
s4="Kaira sends 34 pound to laveena"
s5="Leena sends 90 pound to Rajveer"


First=blockCoin("intial string", [s1,s2,s3])
print(First.blockData)
print(First.block_hash)		