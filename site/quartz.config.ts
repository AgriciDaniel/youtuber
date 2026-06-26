import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "YouTube Brain",
    pageTitleSuffix: " · YouTube Brain",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "agricidaniel.github.io/youtuber",
    ignorePatterns: ["private", "templates", ".obsidian", "meta", "hot.md", "log.md"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Roboto",
        body: "Roboto",
        code: "Roboto Mono",
      },
      colors: {
        lightMode: {
          light: "#ffffff",
          lightgray: "#e5e5e5",
          gray: "#909090",
          darkgray: "#4e4e4e",
          dark: "#0f0f0f",
          secondary: "#ff0000",
          tertiary: "#cc0000",
          highlight: "rgba(255, 0, 0, 0.10)",
          textHighlight: "#ff000033",
        },
        darkMode: {
          light: "#0f0f0f",
          lightgray: "#272727",
          gray: "#717171",
          darkgray: "#d4d4d4",
          dark: "#ffffff",
          secondary: "#ff4e45",
          tertiary: "#ff6d6d",
          highlight: "rgba(255, 0, 0, 0.15)",
          textHighlight: "#ff000044",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // CustomOgImages() omitted for a faster first build
    ],
  },
}

export default config
