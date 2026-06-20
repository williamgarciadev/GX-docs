---
title: "Reading and writing chunked responses"
source_id: 55630
source_url: https://wiki.genexus.com/commwiki/wiki?55630
genexus_version: "18"
---

# Reading and writing chunked responses

Response chunking is a technique used in the HTTP protocol to send response data incrementally instead of delivering the entire response at once.

In a conventional response, the server sends the complete response content to the client server in a single block, which can result in long wait times for large responses. Chunked responses address this issue by dividing the response into smaller fragments or "chunks" and sending them sequentially.

When using a chunked response, the server sends an additional header called "Transfer-Encoding" with the value "chunked" to indicate that the response will be sent in chunks. Each response fragment is sent with its individual length, which enables the client server to process them incrementally as they are received.

### [Benefits of chunked responses](#Benefits+of+chunked+responses)

The benefits of chunked responses are as follows:

* Faster response times: By sending smaller fragments of the response incrementally, the client server can begin processing and displaying the data before the entire response is received. This reduces the user's perceived wait time and improves loading speed.
* Efficient use of server resources: By sending response fragments instead of waiting for the entire response to complete, the server can free up resources and connections more quickly. This allows more simultaneous requests to be handled and improves server scalability.
* Data Streaming: Chunked responses allow data to be sent in real time or in streams, which is especially useful for applications that stream multimedia content, such as videos or audio. The client server can start playing the received fragments before the entire stream is received.

### [Reading chunked responses](#Reading+chunked+responses)

To implement response reading in fragments in GeneXus, use the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) with the [ReadChunk method](https://wiki.genexus.com/commwiki/wiki?55645) and the [EOF Property](https://wiki.genexus.com/commwiki/wiki?6975), as shown in the following example:

```
&HttpClient.Execute(!"GET", &URL)
do while not &HttpClient.EOF
             &ChunkDataString = &HttpClient.ReadChunk()
             &SDT.FromJson(&ChunkDataString)
             &ReceivedText += &SDT.Value
enddo
```

In the example, an HTTP GET request is made, and as long as data is available in the HTTP response (i.e. as long as the EOF property is not true), a loop is executed.  
  
In each iteration of the loop, the ReadChunk() method is used to read a fragment of the response. This response fragment is stored in the &ChunkDataString variable.

Since, in this example, the ReadChunk response is a string containing a JSON, you must create an SDT with the structure of that JSON. To achieve this, you must define a variable (&SDT) based on that SDT and load the &ChunkDataString into &SDT using the [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809).

Finally, these chunks are added to a variable called &ReceivedText, which acts as a container to accumulate all the data chunks of the response.

If the content sent by the service is not chunked, using ReadChunk returns the same result as [&HttpClient.ToString()](https://wiki.genexus.com/commwiki/wiki?7090). In addition, EOF is set to true.

### [Writing chunked responses](#Writing+chunked+responses)

To indicate that the response is not going to be buffered but chunked—that is, that the content is sent at the same moment the response is written—follow the steps below:

1. Define a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) with the [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) set to HTTP and the [Buffer Response property](https://wiki.genexus.com/commwiki/wiki?55195) set to Disabled.
2. Define a variable of [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) and use the [AddString method](https://wiki.genexus.com/commwiki/wiki?7063), as shown below:

   ```
   for &i=1 to 10
          &HttpResponse.AddString(&i.ToString().Trim() + newline())
          &j = sleep(1)
   endfor

   &HttpResponse.AddString("END" + newline())
   ```

### [Scope](#Scope)

**Generator**: [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

**Note**: In Angular, only reading chunked responses is supported.

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).


|  |
| --- |
| **Backlinks** |
| [Buffer Response property](https://wiki.genexus.com/commwiki/wiki?55195) | [EOF Property](https://wiki.genexus.com/commwiki/wiki?6975) |
| [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241) | [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) | [ReadChunk method](https://wiki.genexus.com/commwiki/wiki?55645) |

---
