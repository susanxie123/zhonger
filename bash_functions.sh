快去做(){
    echo "好的，我马上就做!"
    sleep 0.5
    echo "等我一下..."
    sleep 0.5
    python compiler.py $1.中
    echo "做完啦！😄 "
    echo ""
    python $1.py
    echo ""
    sleep 0.5
    echo "快夸夸我做得好不好？（好的／不好）"
    select yn in "好的" "不好"; do
        case $yn in
            好的 ) echo "😘 "; break;;
            不好 ) echo "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 ";;
        esac
    done
}
