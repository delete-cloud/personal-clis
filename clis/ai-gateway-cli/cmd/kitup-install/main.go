package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"path/filepath"

	kitup "github.com/lathe-cli/kitup/go"
)

func main() {
	apply := flag.Bool("apply", false, "write kitup-owned skill installs (default is plan only)")
	flag.Parse()
	cwd, err := os.Getwd()
	if err != nil {
		fatal(err)
	}
	skillDir := filepath.Join(cwd, "skills", "ai-gateway-cli")
	opts := kitup.InstallOptions{
		AppID:       "ai-gateway-cli",
		SkillBundle: kitup.DirectoryBundle(skillDir),
		Scope:       kitup.UserScope,
		Agents:      kitup.AutoAgents(),
	}
	if !*apply {
		report, err := kitup.PlanBundledSkill(opts)
		if err != nil {
			fatal(err)
		}
		enc := json.NewEncoder(os.Stdout)
		enc.SetIndent("", "  ")
		if err := enc.Encode(report); err != nil {
			fatal(err)
		}
		if len(report.Errors)+len(report.Conflicts) > 0 {
			os.Exit(1)
		}
		return
	}
	report, err := kitup.RunBundledSkillInstall(kitup.InstallWorkflowOptions{
		InstallOptions: opts,
		Yes:            true,
		DryRun:         false,
		Out:            os.Stdout,
		Err:            os.Stderr,
	})
	if err != nil {
		fatal(err)
	}
	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")
	_ = enc.Encode(report)
	if report.Canceled || len(report.Report.Errors)+len(report.Report.Conflicts)+len(report.Plan.Conflicts)+len(report.Plan.Errors) > 0 {
		os.Exit(1)
	}
}

func fatal(err error) {
	fmt.Fprintf(os.Stderr, "kitup-install: %v\n", err)
	os.Exit(1)
}
