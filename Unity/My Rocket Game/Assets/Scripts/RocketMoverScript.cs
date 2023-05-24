using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RocketMoverScript : MonoBehaviour
{
    Rigidbody Rigidbody;

    // Start is called before the first frame update
    void Start()
    {
        Rigidbody = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Rigidbody != null)
        {
            if (Input.GetKey(KeyCode.W))
            {
                Rigidbody.AddForce(new Vector3(0, 1));
            }

			if (Input.GetKey(KeyCode.S))
			{
				Rigidbody.AddForce(new Vector3(0, -1));
			}

			if (Input.GetKey(KeyCode.A))
			{
				Rigidbody.AddForce(new Vector3(-1, 0));
			}

			if (Input.GetKey(KeyCode.D))
			{
				Rigidbody.AddForce(new Vector3(1, 0));
			}

            Rigidbody.transform.rotation = Quaternion.LookRotation(Rigidbody.velocity, transform.up);
		}
	}
}
