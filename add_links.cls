VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisWorkbook"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub addHyperlink()

'Dim TargetBook As Workbook
Dim TargetSheet As Worksheet
Dim Target As Variant

'Set TargetBook = ThisWorkbook
Set TargetSheet = ActiveSheet

For Each Target In TargetSheet.Range("D2:D300")
    If Target <> "" Then
        Target.Hyperlinks.Add Anchor:=Target, Address:=Target.Value, TextToDisplay:=Target.Value
    End If
Next Target

End Sub


Sub addEmail()

'Dim TargetBook As Workbook
Dim TargetSheet As Worksheet
Dim Target As Variant

'Set TargetBook = ThisWorkbook
Set TargetSheet = ActiveSheet

For Each Target In TargetSheet.Range("C2:C300")
    If Target <> "" Then
        Target.Hyperlinks.Add Anchor:=Target, Address:="Mailto:" & Target.Value, TextToDisplay:=Target.Value
    End If
Next Target

End Sub
