# coding = utf-8

def on_success( result ):
    print(result)

def ajax( dic ):
    # fasong iyge qingqgiu
    # shou daole yige result

ajax( {
    "success" : on_success
} )
