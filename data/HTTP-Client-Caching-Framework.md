View Source

## Overview

The i3http library -- see corei3http -- already provides a framework for implementing HTTP servers, but its client-side facilities are still somewhat primitive; sufficient for simple tasks, but requiring quite a bit of work from the application programmer when more complex client behavior is required. The primary such behavior is client-side caching, where copies of frequently accessed resources are kept locally, and the server access is kept to a minimum. The media server currently implements caching of prompt files -- see //depot/systest/eic/main/products/eic/src/mediaserver/ininmediaserver/ -- and our intention is to generalize this implementation into a framework provided by the i3http library and easily adaptable for a wide range of applications.

## Design

### Design Notes

## Outstanding Issues

SCR  |  Summary  |  Assignee  |  Fix Version   
---|---|---|---
