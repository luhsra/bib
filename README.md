The Bibliographic Repository of the Systems Research and Architecture Group (SRA)
=================================================================================

- `sra-own.bib`: All publications that were authored by
  members of the group. This file contains *no* @crossref entries. All
  @proceedings entries are actually workshops or conferenceses that
  were edited by an SRA member.

- `sra-ext.bib`: Shared bibliography file of all further refrences. 
  This file *makes use of  @crossref entries* (albeit not systematically). 

**Note** _The SRA bibliography itself is hosted at github at `https://github.com/luhsra/bib.git`. You may have found, however, this file somewhere on your local disc. If that is the case, it is very likely that you have found it in the local checkout/clone of some other svn/git repository, where it is embedded via git-submodule or svn:externals._

## Policies

This section provides recommended practices how to add new references.
However, expect to find _a lot of_ entries that do not follow this guidance.

### Website citations

Do it with `online`:
```
@online{dpdkSite,
  title={Data Plane Development Kit (DPDK)},
  author={Intel},
  url={https://www.dpdk.org/},
  urldate={2023-02-21},
  year={2023}
}
```

### URLs to PDFs

There seems not to be a specific field for PDF links (in the BibLaTeX documentation, `url` is the closest but separately printed).
Therefore, we use an extra field `x-pdf` for that.

### Editions

The edition field is language dependent and it is not clear wheather an extra point is made or not, e.g. compare:
```
2. edition
second edition
2nd edition
2 edition
2. Auflage
second Auflage
2 Auflage
````

Therefore, the preferred way here is the number together with a dot: `edition = {2.},`.

### DOI URLs

Do not write down these URLs! Specify the DOI directly: `doi = {...},`.
