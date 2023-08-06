#pragma once

#include <arbor/export.hpp>

namespace arb {
ARB_ARBOR_API extern const char* source_id;
ARB_ARBOR_API extern const char* arch;
ARB_ARBOR_API extern const char* build_config;
ARB_ARBOR_API extern const char* version;
ARB_ARBOR_API extern const char* full_build_id;
constexpr int version_major = 0;
constexpr int version_minor = 7;
constexpr int version_patch = 0;
ARB_ARBOR_API extern const char* version_dev;
}

#define ARB_SOURCE_ID "2022-07-19T13:38:23+02:00 d0e424b462c78a7a6b07a6ca6121830268fb40b8"
#define ARB_ARCH "none"
#define ARB_BUILD_CONFIG "RELEASE"
#define ARB_FULL_BUILD_ID "source_id=2022-07-19T13:38:23+02:00 d0e424b462c78a7a6b07a6ca6121830268fb40b8;version=0.7;arch=none;config=RELEASE;NEUROML_ENABLED;BUNDLED_ENABLED;"
#define ARB_VERSION "0.7"
#define ARB_VERSION_MAJOR 0
#define ARB_VERSION_MINOR 7
#define ARB_VERSION_PATCH 0
#define ARB_NEUROML_ENABLED
#define ARB_BUNDLED_ENABLED
