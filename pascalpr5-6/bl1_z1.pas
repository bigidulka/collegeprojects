var A: array[1..20] of integer;
k, pr,sum,a,b:integer;
begin
k:=0; pr:=1; sum:=0;
readln(a,b);
for i:integer:=1 to 20 do a[i]:=random(-22,93); 
for i:integer:=1 to 20 do begin
  if(a[i] mod 2 =0) and (i mod 2 <>0)then k+=1;
  if(a[i]mod 2 <>0)then pr*=a[i];
end; 
for i:integer:=a to b do begin
end; 
for i:integer:=1 to 20 do write(A[i], ' ');
writeln();
writeln(k,' ',pr);
end.