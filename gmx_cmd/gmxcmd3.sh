!#/bin/sh
gmx grompp -f em-sol-pme.mdp -c fws-b4em.gro -p fws.top -o em-sol.tpr
sleep 4s
gmx mdrun -v -deffnm em-sol
sleep 4s
gmx grompp -f nvt-pr-md.mdp -c em-sol.gro -p fws.top -o nvt-pr.tpr
sleep 4s
gmx mdrun -deffnm nvt-pr
