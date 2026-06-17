{{/*
Nom complet de la release (tronqué à 63 caractères, convention Kubernetes).
*/}}
{{- define "tic-tac-toe.fullname" -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Nom du chart.
*/}}
{{- define "tic-tac-toe.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Labels communs appliqués à toutes les ressources.
*/}}
{{- define "tic-tac-toe.labels" -}}
helm.sh/chart: {{ include "tic-tac-toe.chart" . }}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Labels de sélecteur (stables, utilisés dans matchLabels et selector).
*/}}
{{- define "tic-tac-toe.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}