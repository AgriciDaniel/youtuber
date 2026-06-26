import { QuartzEmitterPlugin } from "../types"
import { write } from "./helpers"
import { styleText } from "util"
import { FullSlug } from "../../util/path"

export function extractDomainFromBaseUrl(baseUrl: string) {
  const url = new URL(`https://${baseUrl}`)
  return url.hostname
}

export const CNAME: QuartzEmitterPlugin = () => ({
  name: "CNAME",
  async emit(ctx) {
    if (!ctx.cfg.configuration.baseUrl) {
      console.warn(
        styleText("yellow", "CNAME emitter requires `baseUrl` to be set in your configuration"),
      )
      return []
    }
    const content = extractDomainFromBaseUrl(ctx.cfg.configuration.baseUrl)
    if (!content) {
      return []
    }

    const path = await write({
      ctx,
      content,
      slug: "CNAME" as FullSlug,
      ext: "",
    })
    return [path]
  },
  async *partialEmit() {},
})
