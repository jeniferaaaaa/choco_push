■使用推奨環境
ブラウザ:Chrome 79.0.xxxx.xx
OS:Windows10
Python:3.7.3(3系であればよい)

※Chromeはこのバージョンでないと現状動かないので注意


■Pythonインポート必須ライブラリ
・selenium
・datetime

上記をpipでインストールしてください。

■仕様
・ちょこきんの出社ボタンを自動で押してくれます。
・A勤の「8:30～8:59」、B勤の「09:30～9:59」の間のみ動作します。
・成功するとsuccess.logに日時付きで知らせてくれます。
・失敗するとerror.logに日時付きで知らせてくれます。
・ログは全て同一ファイルで完結するため、タイムスタンプに注意してください。

■使用方法
　1.設定
    configフォルダにあるconfig.pyが設定ファイルになります。
    そこに自分がちょこ勤で入力している社員番号とパスワードを打ち込んで保存してください。

  2.プログラムをスタートアップに組み込む
    ①「start.bat」のショートカットを作成してください。

    ②下記パスへアクセスしてください。
      C:\Users\a社員番号\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

    ③先ほど作成したショートカットをここに配置してください。

  3.おわり

 
■環境
chromedriverバージョン：79.0.3945.36

