{{/*
Create a default fully qualified app name.
*/}}
{{- define "tic-tac-toe.fullname" -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- end }}