!#/bin/sh
gmx grompp -f em-sol-pme.mdp -c fws-b4em.gro -p fws.top -o em-sol.tpr
sleep 4s
gmx mdrun -v -deffnm em-sol
sleep 4s
gmx grompp -f nvt-pr-md.mdp -c em-sol.gro -p fws.top -o nvt-pr.tpr
sleep 4s
gmx mdrun -deffnm nvt-pr   运行到这一步没问题。运行时间长
sleep 4s
gmx grompp -f npt-pr-md.mdp -c nvt-pr.gro -p fws.top -o npt-pr.tpr
sleep 4s
gmx mdrun -deffnm npt-pr
sleep 4s
gmx grompp -f npt-nopr-md.mdp -c npt-pr.gro -p fws.top -o npt-nopr.tpr
sleep 4s
#nohup gmx mdrun -deffnm npt-nopr &