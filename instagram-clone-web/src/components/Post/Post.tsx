import React, { FC, useEffect, useState } from 'react'
import { PostType } from '../../features/posts/postsSlice'
import Avatar from '../Widgets/Avatar'
import Button from '../Widgets/Button'
import Image from '../Widgets/Image'
import './Post.scss'

interface PropsType {
  item: PostType
}

const Post: FC<PropsType> = ({ item }) => {
  // const [comments, setComments] = useState([])

  // useEffect(() => {
  //   setComments(item?.comments?.length > 0 ? item?.comments : [])
  // }, [])
  return (
    <div className='post'>
      <div className='post_header'>
        <Avatar />
        <div className='post_header-info'>
          <h3>{item.user.username}</h3>
          <div className='delete'>
            <Button>Delete</Button>
          </div>
        </div>
      </div>
      <Image
        url={item.image_url}
        type={item.image_url_type}
        className='post_image'
      />

      <h4 className='post_text'>{item.caption}</h4>

      <div className='post_comments'>
        {item?.comments?.length > 0 &&
          item?.comments?.map((comment, idx) => (
            <p key={idx}>
              <strong>{comment.username}:</strong> {comment.text}
            </p>
          ))}
      </div>
    </div>
  )
}

export default Post
