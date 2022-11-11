program z4_for;
var i,sum:integer;
begin
  for i:=4 to 37 do begin 
    sum:=sum+(i*i);
  end;
    writeln($'{sum}');
end.