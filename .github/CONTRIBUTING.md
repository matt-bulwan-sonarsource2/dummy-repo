Please ensure your accept the following limitations when releasing "sonarcloud-observability":

- [ ] The release of this repository is of "alpha" type. The Cloud Platform squad reserves the right to make fundamental changes to the process, content and structure of the artifact.
- [ ] The build will be published to artifactory under the name of "sc_observability_alpha"
- [ ] Currently, only the "sonarcloud-codedatalake" repository is using this process and the artifact. 


**Tagging Guidelines:**

* **Follow Semantic Versioning (SemVer):** `MAJOR.MINOR.PATCH`
    * `MAJOR`: Incremented for incompatible API changes.
    * `MINOR`: Incremented for adding functionality in a backward-compatible manner.
    * `PATCH`: Incremented for backward-compatible bug fixes.
* **Prefix with 'v':** All tags should start with `v` (e.g., `v1.0.0`, `v2.1.5`).
* **Annotated Tags:** Always create **annotated tags** (`git tag -a v1.0.0 -m "Release v1.0.0"`). This includes a message, tagger's name, and date, making them more robust and secure for releases.
* **Consistency:** Maintain consistent naming conventions.
* **Pre-releases:** For pre-release versions (alpha, beta, release candidate), append a hyphen and identifier (e.g., `v1.0.0-alpha.1`, `v1.0.0-beta`, `v1.0.0-rc.1`).
* **Do not re-tag:** Never re-tag an existing version with different content. If you need to fix something, create a new patch release.

**Implications of Tagging:**

* **Version Control:** Tags provide a permanent snapshot of your code at a specific point in history, making it easy to revert to or check out previous versions.
* **Release Management:** GitHub Releases are directly tied to Git tags. A tag is essential for creating a release.
* **Automated Workflows:** Many CI/CD pipelines and automation tools trigger actions based on new tags being pushed.
* **Clarity for Users:** Clear and consistent tagging helps users understand the nature of changes between releases and which version they are using.
* **Discoverability:** Users can easily find and download specific versions of your software via the releases page.