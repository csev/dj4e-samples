import { html, LitElement } from "https://cdn.jsdelivr.net/npm/lit@3.2.1/+esm";

export class DJ4EFavoriteStar extends LitElement {

  static properties = {
    fav: { type: Boolean },
  };

  // Don't use Shadow-DOM 
  createRenderRoot() { return this; }

  render() {

    return html`
      <span class="fa-stack" style="vertical-align: middle;">
        <i class="fa fa-star fa-stack-1x" style="${this.fav ? "" : "display: none;"} color: orange;"></i>
        <i class="fa fa-star-o fa-stack-1x"></i>
      </span>
    `
  }
}

customElements.define('dj4e-favstar', DJ4EFavoriteStar);

