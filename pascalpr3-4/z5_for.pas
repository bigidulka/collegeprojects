program z5_for;
var i,n:integer;
begin
  write('Напишите число для деления: '); readln(n);
  for i:=n downto 1 do begin 
    if n mod i=0 then write(i, ' ');
  end;
end.