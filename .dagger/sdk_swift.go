package main

import (
	"context"
	"fmt"
	"regexp"
	"strings"

	"go.opentelemetry.io/otel/codes"
	"golang.org/x/sync/errgroup"

	"github.com/dagger/dagger/.dagger/internal/dagger"
)

const (
	swiftSDKPath            = "sdk/swift"
	swiftSDKGeneratedPath   = swiftSDKPath + "/lib/dagger/gen"
	swiftSDKVersionFilePath = swiftSDKPath + "/lib/dagger/core/version.ex"
)
var swiftVersions = map[string]string{
	// TODO: Add older versions
	"6.0.1": "6.0.1-bookworm@sha256:5e9de686d99366e738e208c21b1bca1e0dceb44e6a8af23124747d02ddca9461",
}

const swiftLatestVersion = "6.0.1"

type SwiftSDK struct {
	Dagger *DaggerDev // +private
}

// // Lint the Elixir SDK
// func (t SwiftSDK) Lint(ctx context.Context) error {
// 	eg, ctx := errgroup.WithContext(ctx)
// 	eg.Go(func() (rerr error) {
// 		ctx, span := Tracer().Start(ctx, "lint the Swift source")
// 		defer func() {
// 			if rerr != nil {
// 				span.SetStatus(codes.Error, rerr.Error())
// 			}
// 			span.End()
// 		}()

// 		installer, err := t.Dagger.installer(ctx, "sdk")
// 		if err != nil {
// 			return err
// 		}

// 		_, err = t.swiftBase(swiftVersions[swiftLatestVersion]).
// 			With(installer).
// 			WithExec([]string{"mix", "lint"}).
// 			Sync(ctx)
// 		return err
// 	})
// 	eg.Go(func() (rerr error) {
// 		ctx, span := Tracer().Start(ctx, "check that the generated client library is up-to-date")
// 		defer func() {
// 			if rerr != nil {
// 				span.SetStatus(codes.Error, rerr.Error())
// 			}
// 			span.End()
// 		}()
// 		before := t.Dagger.Source()
// 		after, err := t.Generate(ctx)
// 		if err != nil {
// 			return err
// 		}
// 		return dag.Dirdiff().AssertEqual(ctx, before, after, []string{"sdk/elixir/lib/dagger/gen"})
// 	})
// 	return eg.Wait()
// }

// // Test the Elixir SDK
// func (t SwiftSDK) Test(ctx context.Context) error {
// 	installer, err := t.Dagger.installer(ctx, "sdk")
// 	if err != nil {
// 		return err
// 	}

// 	eg, ctx := errgroup.WithContext(ctx)
// 	for elixirVersion, baseImage := range swiftVersions {
// 		ctr := t.swiftBase(baseImage).With(installer)

// 		ctx, span := Tracer().Start(ctx, "test - elixir/"+elixirVersion)
// 		defer span.End()

// 		eg.Go(func() error {
// 			ctx, span := Tracer().Start(ctx, "dagger")
// 			defer span.End()

// 			_, err := ctr.
// 				WithExec([]string{"mix", "test"}).
// 				Sync(ctx)
// 			return err
// 		})

// 		if elixirVersion == swiftLatestVersion {
// 			eg.Go(func() error {
// 				ctx, span := Tracer().Start(ctx, "dagger_codegen")
// 				defer span.End()

// 				_, err := ctr.
// 					WithWorkdir("dagger_codegen").
// 					WithExec([]string{"mix", "deps.get"}).
// 					WithExec([]string{"mix", "test"}).
// 					Sync(ctx)
// 				return err
// 			})
// 		}
// 	}
// 	return eg.Wait()
// }

// Regenerate the Elixir SDK API
func (t SwiftSDK) Generate(ctx context.Context) (*dagger.Directory, error) {
	installer, err := t.Dagger.installer(ctx, "sdk")
	if err != nil {
		return nil, err
	}
	introspection, err := t.Dagger.introspection(ctx, installer)
	if err != nil {
		return nil, err
	}
	gen := t.swiftBase(swiftVersions[swiftLatestVersion]).
		With(installer).
		WithWorkdir("dagger_codegen").
		WithMountedFile("/schema.json", introspection).
		WithExec([]string{"mix", "dagger.codegen", "generate", "--introspection", "/schema.json", "--outdir", "gen"}).
		WithExec([]string{"mix", "format", "gen/*.ex"}).
		Directory("gen")

	dir := dag.Directory().WithDirectory("sdk/elixir/lib/dagger/gen", gen)
	return dir, nil
}

// // Test the publishing process
// func (t SwiftSDK) TestPublish(ctx context.Context, tag string) error {
// 	return t.Publish(ctx, tag, true, nil, "https://github.com/dagger/dagger.git", nil)
// }

// // Publish the Elixir SDK
// func (t SwiftSDK) Publish(
// 	ctx context.Context,
// 	tag string,

// 	// +optional
// 	dryRun bool,
// 	// +optional
// 	hexAPIKey *dagger.Secret,

// 	// +optional
// 	// +default="https://github.com/dagger/dagger.git"
// 	gitRepoSource string,
// 	// +optional
// 	githubToken *dagger.Secret,
// ) error {
// 	version, isVersioned := strings.CutPrefix(tag, "sdk/elixir/")
// 	mixFile := "/sdk/elixir/mix.exs"

// 	ctr := t.swiftBase(swiftVersions[swiftLatestVersion])

// 	if !dryRun {
// 		mixExs, err := t.Dagger.Source().File(mixFile).Contents(ctx)
// 		if err != nil {
// 			return err
// 		}
// 		newMixExs := strings.Replace(mixExs, `@version "0.0.0"`, `@version "`+strings.TrimPrefix(version, "v")+`"`, 1)
// 		ctr = ctr.WithNewFile(mixFile, newMixExs)
// 	}

// 	if dryRun {
// 		ctr = ctr.
// 			WithEnvVariable("HEX_API_KEY", "").
// 			WithExec([]string{"mix", "hex.publish", "--yes", "--dry-run"})
// 	} else {
// 		ctr = ctr.
// 			WithSecretVariable("HEX_API_KEY", hexAPIKey).
// 			WithExec([]string{"mix", "hex.publish", "--yes"})
// 	}
// 	_, err := ctr.Sync(ctx)
// 	if err != nil {
// 		return err
// 	}

// 	if isVersioned {
// 		if err := githubRelease(ctx, githubReleaseOpts{
// 			tag:         tag,
// 			notes:       sdkChangeNotes(t.Dagger.Src, "elixir", version),
// 			gitRepo:     gitRepoSource,
// 			githubToken: githubToken,
// 			dryRun:      dryRun,
// 		}); err != nil {
// 			return err
// 		}
// 	}

// 	return nil
// }

// var elixirVersionRe = regexp.MustCompile(`@dagger_cli_version "([0-9\.-a-zA-Z]+)"`)

// // Bump the Elixir SDK's Engine dependency
// func (t SwiftSDK) Bump(ctx context.Context, version string) (*dagger.Directory, error) {
// 	contents, err := t.Dagger.Source().File(swiftSDKVersionFilePath).Contents(ctx)
// 	if err != nil {
// 		return nil, err
// 	}

// 	newVersion := fmt.Sprintf(`@dagger_cli_version "%s"`, strings.TrimPrefix(version, "v"))
// 	newContents := elixirVersionRe.ReplaceAllString(contents, newVersion)

// 	return dag.Directory().WithNewFile(swiftSDKVersionFilePath, newContents), nil
// }

func (t SwiftSDK) swiftBase(baseImage string) *dagger.Container {
	src := t.Dagger.Source().Directory(swiftSDKPath)
	mountPath := "/" + swiftSDKPath

	return dag.Container().
		From(baseImage).
		WithWorkdir(mountPath).
		WithDirectory(mountPath, src).
		WithExec([]string{"mix", "deps.get"})
}
