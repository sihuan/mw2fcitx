#!/bin/bash
set -e

pushd /toolkit

mihoyo=(genshin honkai3rd starrail)

pacman -Syu --noconfirm libime python-pip python-virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

for game in ${mihoyo[@]}; do
    mw2fcitx -c utils/${game}_dict.py
done

useradd archbuild
chmod -R a+rwx .
export DATE=$(date +%Y%m%d)
su archbuild utils/makepkg.sh

for game in ${mihoyo[@]}; do
    cp fcitx5-pinyin-${game}* /artifacts
    cp ./${game}.dict /artifacts
    cp ./${game}.dict.yaml /artifacts
    cp ./${game}_titles.txt /artifacts
done

popd
