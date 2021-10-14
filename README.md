# anaconda-workspace
anaconda環境を立ち上げる
```bash
docker-compose up
```
anaconda環境をバックグラウンドで立ち上げる
```bash
docker-compose up -d
```
ブラウザからJupyter Lab に入る
```bash
http://localhost:8080/
```
anaconda環境を停止させる
```
docker-compose down
```
環境リセットの滅びの呪文
```
docker-compose down --rmi all --volumes
```

# 参考
- [【画像で説明】DockerでAnaconda環境をつくり、コンテナの中でVSCodeを使う - Qiita](https://qiita.com/komiya_____/items/96c14485eb035701e218#-docker-compose%E3%81%A7%E8%B5%B7%E5%8B%95%E3%81%99%E3%82%8B%E5%A0%B4%E5%90%88)
- [《滅びの呪文》Docker Composeで作ったコンテナ、イメージ、ボリューム、ネットワークを一括完全消去する便利コマンド - Qiita](https://qiita.com/suin/items/19d65e191b96a0079417)