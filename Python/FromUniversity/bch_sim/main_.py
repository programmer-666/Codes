import json
class Bch_sim:
    def List_Terminals(self, file_name):
        with open(file_name) as ofile:
            self.terminals = json.loads(ofile.read())

sys = Bch_sim()
sys.List_Terminals("terminals.json")
print(sys.terminals)