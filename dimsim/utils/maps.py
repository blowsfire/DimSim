consonantMap_TwoDCode ={
    "b":(1.0,0.5),
    "p":(1.0,1.5), 

    "g":(7.0,0.5), 
    "k":(7.0,1.5), 
    "h":(7.0,3.0), 
    "f":(7.0,4.0), 

    "d":(12.0,0.5), 
    "t":(12.0,1.5), 

    "n":(22.5,0.5), 
    "l":(22.5,1.5), 
    "r":( 22.5,2.5), 

    
    "zh":(30,1.7), 
    "z":(30,1.5), 
    "j":(30.0,0.5), 

    "ch":(31,1.7), 
    "c":(31,1.5), 
    "q":(31.0,0.5), 

    "sh":(33,3.7),
    "s":(33,3.5),
    "x":(33,2.5),

    
    "m":(50.0,3.5), 

    "y":(40.0,0.0), 
    "w":(40,5.0),
    
    "":(99999.0,99999.0)
}

vowelMap_TwoDCode = {
    "a":(1.0,0.0),
    "an":(1.0,1.0),
    "ang":(1.0,1.5),

    
    "ia":(0.0,0.0),
    "ian":(0.0,1.0),
    "iang":(0.0,1.5),

    "ua":(2.0,0.0),
    "uan":(2.0,1.0),
    "uang":(2.0,1.5),
    "u:an":(2.0,1.0),

    
    "ao":(5.0,0.0),
    "iao":(5.0,1.5),

    "ai":(8.0,0.0),
    "uai":(8.0,1.5),

    

    "o":(20,0.0),
    "io":(20,2.5),
    "iou":(20,4),
    "iu":(20,4),
    "ou":(20,5.5),
    "uo":(20,6.0),

    "ong":(20,8.0),
    "iong":(20,9.5),

    
    "er":(41,1),
    "e":(41,0.0),

    "u:e":(40,5.0),
    "ve":(40,5.0),
    "ue":(40,5.0),
    "ie":(40,4.5),
    "ei":(40,4.0),
    "uei":(40,3.0),
    "ui":(40,3.0),

    "en":(42,0.5),
    "eng":(42,1.0),

    "uen":(43,0.5),
    "un":(43,0.5),
    "ueng":(43,1.0),

    
    "i":(60,1.0),
    "in":(60,2.5),
    "ing":(60,3.0),

    "u:":(61,1.0),
    "v":(61,1.0),
    "u:n":(61,2.5),
    "vn":(61,2.5),

    "u":(80,0.0),

    "":(99999.0,99999.0)
}

consonantList = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k","h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s","y", "w"]

vowelList = ["a", "o", "e", "i", "u", "v","u:","er", "ao","ai", "ou","ei", "ia", "iao", "iu", "iou","ie", "ui","uei","ua","uo","uai", "u:e","ve",  "an", "en", "in", "un","uen", "vn","u:n","ian","uan", "u:an","van", "ang", "eng", "ing", "ong","iang","iong","uang","ueng"]

hardcodeMap = {
    "hua":"fa",
    "fa":"hua",
    "huan":"fan",
    "fan":"huan",
    "hui":"fei",
    "jie":"zhe",
    "kou":"ke",
    "gou":"ge",
    "zhong":"zen",
    "san":"shang"
}

consonantMap = {
    "b":1.0,
    "p":2.0,
    
    "m":11.0,
    "f":12.0,
    
    "d":21.0,
    "t":22.0,
    
    "n":31.0,
    "l":31.0,
    "r":32.0,
    
    "g":41.0,
    "k":42.0,
    "h":43.0,
    
    "j":46.0,
    "q":47.0,
    "x":48.0,
    
    "z":61.0,
    "c":62.0,
    
    "zh":71.0,
    "ch":72.0,
    
    "sh":81.0,
    "s":82.0,
    
    "y":90.0,
    "w":100.0,
    
    "":99999.0,
    "__v":99999.0
}

vowelMap = {
    "ia":0.0,
    "a":2.0,
    "ai":3.0,
    "uai":4.0,
    "iao":6.0,
    "ao":7.0,
    
    "uan":10.0,
    "an":11.0,
    "ang":12.0,
    "ian":14.0,
    "iang":15.0,
    "uang":17.0,
    "ua":18.0,
    
    "o":21.0,
    "io":22.0,
    "ou":23.0,
    "uo":24.0,
    "ong":26.0,
    "iong":27.0,
    
    "e":31.0,
    "ei":33.0,
    "ie":34.0,
    "er":37.0,
    
    "ve":40.0,
    "ue":40.0,
    "u:e":40.0,
    
    "en":43.0,
    "eng":44.0,
    
    "uen":45.0,
    "ueng":45.0,
    
    "u:en":42.0,
    "ven":42.0,
    
    "i":50.0,
    "u:":51.0,
    "v":51.0,
    "u:n":53.0,
    "vn":53.0,
    "u:an":55.0,
    "v:an":55.0,
    
    "in":53.0,
    "ing":55.0,
    
    "u":60.0,
    "ui":63.0,
    "uei":63.0,
    "iu":64.0,
    "iou":64.0,
    "un":66.0,
    
    "":99999.0,
    "__v":99999.0
}