import pickle
##文件写
save_file=open("save.dat","wb")
game_data={"position":"N2 E3","pocket":["key","knife"],"money":160}
print(game_data)
pickle.dump(game_data,save_file)
save_file.close()

##文件读
load_file=open("save.dat","rb")
load_game_data=pickle.load(load_file)
load_game_data