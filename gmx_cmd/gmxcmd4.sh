gmx grompp -f npt-pr-md.mdp -c nvt-pr.gro -p fws.top -o npt-pr.tpr
sleep 4s
gmx mdrun -deffnm npt-pr
sleep 4s
gmx grompp -f npt-nopr-md.mdp -c npt-pr.gro -p fws.top -o npt-nopr.tpr
sleep 4s

echo 开始进行最后一步了
nohup gmx mdrun -deffnm npt-nopr &