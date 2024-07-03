#!/bin/bash
cp utils/PKGBUILD.* .
sed -i "s/99999999/${DATE}/" PKGBUILD.*

mihoyo=(genshin honkai3rd starrail)

for game in ${mihoyo[@]}; do
    cp PKGBUILD.pinyin PKGBUILD.pinyin.${game}
    cp PKGBUILD.rime PKGBUILD.rime.${game}
    sed -i "s/mihohim/${game}/" PKGBUILD.pinyin.${game}
    sed -i "s/mihohim/${game}/" PKGBUILD.rime.${game}
    makepkg -p PKGBUILD.pinyin.${game}
    makepkg -p PKGBUILD.rime.${game}
done
