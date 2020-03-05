#!/usr/bin/python3 -V
#関数▼
def random_sreep():
    random_int = random.randint(1,2)#ランダムに数字を生成
    if random_int == 1:
        time.sleep(0.1)
    else:
        time.sleep(0.2)
#関数▲
print("このPythonファイルの作成者は、このプログラム実行中に何らかの問題が発生し、損害が発生した場合も一切責任を取りません。ご利用は利用者の自己責任で利用してください。プログラムを開始するには y を入力しEnterキーを押してください。")#注意の表示

user_input = str(input("y? >"))
if user_input == "y":

    #初期化▼
    error = "no"#エラーがない場合、error変数を常にno状態にしておく
    #初期化▲

    #import▼
    try:
        import os
    except:
        error = "yes"
        print("import os で問題が発生しました。")#エラーメッセージ

    try:
        import time
    except:
        error = "yes"
        print("import time で問題が発生しました。")#エラーメッセージ

    try:
        import pyperclip
    except:
        error = "yes"
        print("import pyperclip で問題が発生しました。次のコマンドを実行すると解決する場合があります。'pip3 install pyperclip'")#エラーメッセージ

    try:
        import random
    except:
        error = "yes"
        print("import random で問題が発生しました。")#エラーメッセージ

    #import▲

    default = "Share_Clipboard_Start"#クリップボードの初期値

    #ファイルの書き込みテスト▼
    try:
        tmp_file = os.path.dirname(os.path.abspath(__file__))#データを保存するパスを指定
        tmp_file = str(tmp_file) + "/.Share_Clipboard_tmp.txt";#ファイルを保存するパスを指定
        #ファイルを書き込む▼
        f = open(tmp_file,"w")
        f.write(default)#書き込みをテストする
        f.close()
        #ファイルを書き込む▲
    except:
        error = "yes"
        print(str(tmp_file) + "を作成しようとしましたが、作成に失敗しました。")
    #ファイルの書き込みテスト▲

    if error == "yes":
        #エラーが発生している場合
        print("エラーが発生しているため、プログラムを終了しました。")
    else:
        #エラーが発生していない場合
        print("Share_Clipboard_text.pyが起動しました。1秒毎にクリップボードを同期します。※同期されない場合、ホストOSとゲストOS間で共有フォルダーが設定してある事を確認し、そのフォルダー内にあるShare_Clipboard_text.pyがホストOSとゲストOSの両方で実行されている事を確認して下さい。")#起動メッセージ

        #メインのプログラム▼

        #初期化▼
        roop_exit = 0#whileループを終了するタイミングを管理する
        type_error = 0#クリップボードがテキスト以外である場合、エラーメッセージを連続して出力しないように管理する
        now_bord = default#現在のクリップボード状態
        kysh_bord = default#クリップボードのキャッシュ
        #初期化▲



        while roop_exit == 0:
            try:
                time.sleep(1)
                try:
                    now_bord = pyperclip.paste()#クリップボードの情報を取得
                except:
                    print("クリップボードの情報を取得できません")#エラーメッセージ出力
                    print("  'sudo apt-get install xsel'  を実行すると解決する場合があります。")
                    continue#ループのはじめに戻る
                
                #クリップボードがstr型か確認▼
                try:
                    now_bord = str(now_bord)#str型に変換
                    type_error = 0#次回エラーが発生した時にメッセージが出力されるようにする
                except:
                    if type_error == 0:#連続してエラーが発生していない時
                        print("この形式はサポートしていません")
                        type_error = 1#繰り返してエラーが発生した時にメッセージが出力されないようにする
                    else:#連続してエラーが発生している時
                        pass
                    continue#ループのはじめに戻る
                #クリップボードがstr型確認▲

                if now_bord == kysh_bord:
                    #ファイルとの違いを確認し、違っていればファイル情報を読み込み
                    try:
                        #データの読み込み▼
                        f = open(tmp_file)
                        file_bord = f.read()
                        f.close()
                        #データの読み込み▲
                    except:
                        print("データの読み込みに失敗しました。")
                        random_sreep()#ランダムな時間処理を停止する
                    
                    file_bord = str(file_bord)

                    if now_bord == file_bord:
                        continue
                    else:
                        now_bord = str(file_bord)#データを読み込み
                        kysh_bord = str(file_bord)#データを読み込み
                        pyperclip.copy(now_bord)#クリップボードへ書き込み
                        print("クリップボードを受信しました。")
                        continue
                else:
                    #ファイルにnow_bordを書き込み、kysh_bordにnow_bordを代入
                    try:
                        #データの書き込み▼
                        f = open(tmp_file,"w")
                        f.write(str(now_bord))
                        f.close()
                        #データの書込み▲
                        kysh_bord = str(now_bord)
                        print("クリップボードを送信しました。")
                    except:
                        print("データの書き込みに失敗しました。")
                        random_sreep()#ランダムな時間処理を停止する
                    continue
            except:
                roop_exit = 1
        #メインのプログラム▲
        #終了時の処理▼
        os.remove(tmp_file)
        #終了時の処理▲

else:
    pass
print("プログラムを終了しました。")
