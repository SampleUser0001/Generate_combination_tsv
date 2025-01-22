# Generate_combination_tsv
組み合わせ表を作成する

- [Generate\_combination\_tsv](#generate_combination_tsv)
  - [実行](#実行)
    - [実行結果](#実行結果)

## 実行

``` bash
python app.py sample/pattern_a.txt sample/pattern_b.txt sample/pattern_c.txt 
```

### 実行結果

``` txt
hoge	foo	a
hoge	foo	b
hoge	foo	c
hoge	foo	d
hoge	vaa	a
hoge	vaa	b
hoge	vaa	c
hoge	vaa	d
piyo	foo	a
piyo	foo	b
piyo	foo	c
piyo	foo	d
piyo	vaa	a
piyo	vaa	b
piyo	vaa	c
piyo	vaa	d
fuga	foo	a
fuga	foo	b
fuga	foo	c
fuga	foo	d
fuga	vaa	a
fuga	vaa	b
fuga	vaa	c
fuga	vaa	d
```
