program z1_for;
var dum: real;
i:integer;
begin
  dum:=2.54;
  for i:=1 to 20 do begin 
    writeln(i, ' Д. = ', dum*i, ' CМ.');
  end;
end.